from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import EmailMultiAlternatives

def home(request):
	template_name = 'home/home.html'
	context = {}

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

	context = {
		'form': form,
	}

	return render(request, template_name, context)