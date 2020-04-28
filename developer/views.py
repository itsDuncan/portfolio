from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.core.mail import EmailMultiAlternatives
from django.views.generic import DetailView
from django.conf import settings
from django.template.loader import render_to_string
from django_weasyprint import WeasyTemplateResponseMixin
from django_weasyprint.views import CONTENT_TYPE_PNG
from formtools.wizard.views import SessionWizardView
from .forms import (DeveloperJobForm1, DeveloperJobForm2, DeveloperJobForm3, DeveloperJobForm4, DeveloperJobForm5, DeveloperJobForm6)
from .models import DeveloperJob

class DeveloperJobWizard(SessionWizardView):
	template_name = 'developer/hire.html'
	form_list = [DeveloperJobForm1, DeveloperJobForm2, DeveloperJobForm3, DeveloperJobForm4, DeveloperJobForm5, DeveloperJobForm6]

	def done(self, form_list, form_dict, **kwargs):
		
		data = {key: value for form in form_list for key, value in form.cleaned_data.items()}
		instance = DeveloperJob.objects.create(**data)

		step_0 = self.get_cleaned_data_for_step('0')
		step_1 = self.get_cleaned_data_for_step('1')

		client_name = step_0['senders_name']
		client_email = step_0['senders_email']

		project_name = step_1['project_name']

		project = get_object_or_404(DeveloperJob, project_name=project_name)

		from_email = 'duncanmuiru513@gmail.com'
		to = client_email

		subject = 'Website Development Request'
		text_content = 'Hello {}. Kindly find below an estimate quotation of the services you requested.'.format(client_name)
		html_content = render_to_string('developer/quotation/email_template.html', {'object': project, 'recipient': client_name})

		if subject and text_content and from_email:
			msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
			msg.attach_alternative(html_content, "text/html")
			msg.send()
			messages.success(self.request, ('Your request has been successfully received. Check your email for an estimate quotation'))

		return HttpResponseRedirect('/developer/active-projects/{}'.format(project.slug))

class DeveloperJobDetailView(DetailView):
	model = DeveloperJob
	template_name = 'developer/quotation/web_template.html'

class DeveloperJobrintView(WeasyTemplateResponseMixin, DeveloperJobDetailView):
	pdf_stylesheets = [
		settings.STATIC_ROOT + 'home/css/invoice.css',
	]
	# show pdf in-line (default: True, show download dialog)
	pdf_attachment = True
	pdf_filename = 'web_developer_quotation.pdf'