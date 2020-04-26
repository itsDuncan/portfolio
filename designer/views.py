from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from formtools.wizard.views import SessionWizardView
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.http import HttpResponseRedirect
from .forms import DesignJobForm1, DesignJobForm2
from .models import DesignJob

class DesignJobWizard(SessionWizardView):
	template_name = 'designer/hire_designer.html'
	form_list = [DesignJobForm1, DesignJobForm2]

	def done(self, form_list, form_dict, **kwargs):
		
		data = {key: value for form in form_list for key, value in form.cleaned_data.items()}
		instance = DesignJob.objects.create(**data)

		step_0 = self.get_cleaned_data_for_step('0')
		step_1 = self.get_cleaned_data_for_step('1')

		client_name = step_0['senders_name']
		client_email = step_0['senders_email']

		project = get_object_or_404(DesignJob, senders_name=client_name)

		from_email = 'duncanmuiru513@gmail.com'
		to = client_email

		subject = 'Grpahic Design Request'
		text_content = 'Hello {}. Kindly find below an estimate quotation of the services you requested.'.format(client_name)
		html_content = render_to_string('designer/email/email_template.html', {'recipient': client_name})

		if subject and text_content and from_email:
			msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
			msg.attach_alternative(html_content, "text/html")
			msg.send()
			messages.success(self.request, ('Your request has been sent, you will soon receive an estimate quotation via email'))

		return HttpResponseRedirect('/home/')