from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import EmailMultiAlternatives
from .forms import TrackProjectForm, ContactForm
from django.template.loader import render_to_string

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
		html_content = '<p>This is an <strong>important</strong> message.</p>'

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