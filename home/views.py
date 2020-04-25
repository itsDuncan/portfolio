from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.mail import EmailMultiAlternatives
from .forms import *
from formtools.wizard.views import SessionWizardView
from .models import HireWebDev
from django.views.generic import DetailView
from django.conf import settings

from django_weasyprint import WeasyTemplateResponseMixin
from django_weasyprint.views import CONTENT_TYPE_PNG
from django.http import HttpResponseRedirect


def home(request):
	template_name = 'home/home.html'
	form = TrackProjectForm(request.POST or None)

	context = {
		'form': form,
	}

	return render(request, template_name, context)

def contact(request):
	template_name = 'home/contact.html'

	form = ContactForm(request.POST or None)

	if request.method == 'POST':
		message = request.POST.get('message')
		from_email = request.POST.get('senders_email')
		to = 'duncanmuiru513@gmail.com'

		subject = 'Getting in touch'
		text_content = 'This is an important message.'
		html_content = '<p>This is an <strong>important</strong> message.</p> <i class="fas fa-exclamation-triangle"></i>'

		if subject and message and from_email:
			msg = EmailMultiAlternatives(subject, message, from_email, [to])
			msg.attach_alternative(html_content, "text/html")
			msg.send()

			messages.success(request, ('Your message has been sent, you will soon be contacted'))
			return redirect('home:landing-page')

	context = {
		'form': form,
	}

	return render(request, template_name, context)

def hire_designer(request):
	template_name = 'home/hire_designer.html'
	context = {}

	return render(request, template_name, context)


class HireDevWizard(SessionWizardView):
	template_name = 'home/hire_dev.html'
	form_list = [WebDevHireForm1, WebDevHireForm2, WebDevHireForm3, WebDevHireForm4, WebDevHireForm5, WebDevHireForm6]

	def done(self, form_list, form_dict, **kwargs):
		messages.success(self.request, ('Your request has been sent, you will soon receive an estimate quotation and further directions'))

		data = {key: value for form in form_list for key, value in form.cleaned_data.items()}
		instance = HireWebDev.objects.create(**data)

		project_name_step = self.get_cleaned_data_for_step('1')
		project_name = project_name_step['project_name']

		project = get_object_or_404(HireWebDev, project_name=project_name)

		return HttpResponseRedirect('/active-projects/{}'.format(project.slug))

class HireDevDetailView(DetailView):
	model = HireWebDev
	template_name = 'home/invoice/invoice_pdf_template.html'

class HireDevPrintView(WeasyTemplateResponseMixin, HireDevDetailView):
	# output of MyModelView rendered as PDF with hardcoded CSS
	pdf_stylesheets = [
		settings.STATIC_ROOT + 'home/css/invoice.css',
	]
	# show pdf in-line (default: True, show download dialog)
	pdf_attachment = True
	# suggested filename (is required for attachment!)
	pdf_filename = 'web_developer_quotation.pdf'