from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import EmailMultiAlternatives
from .forms import *
from formtools.wizard.views import SessionWizardView

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

def hire_dev(request):
	template_name = 'home/hire_dev.html'
	context = {}

	return render(request, template_name, context)

def hire_designer(request):
	template_name = 'home/hire_designer.html'
	context = {}

	return render(request, template_name, context)


class HireDevWizard(SessionWizardView):
	template_name = 'home/hire_dev.html'
	form_list = [WebDevHireForm1, WebDevHireForm2, WebDevHireForm3, WebDevHireForm4, WebDevHireForm5, WebDevHireForm6]

	def done(self, form_list, form_dict, **kwargs):
		messages.success(request, ('Your request has been sent, you will soon receive an estimate quotation and further directions'))
		return render(self.request, 'home/home.html', {
			'form_data': [form.cleaned_data for form in form_list],
		})