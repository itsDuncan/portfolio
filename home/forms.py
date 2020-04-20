from django import forms
from home.validators import ascii_validator, email_validator

class ContactForm(forms.Form):
	senders_name = forms.CharField(
		required = True,
		label = '',
		widget = forms.TextInput(
			attrs = {
				'class':'form-control',
				'placeholder': 'Your Name',
		}),
		validators=[ascii_validator]
	)

	senders_email = forms.EmailField(
		required = True,
		label = '',
		widget = forms.TextInput(
			attrs = {
				'class': 'form-control',
				'placeholder': 'Your Email',
		}),
		validators=[email_validator]
	)

	message = forms.CharField(
		required = True,
		label = '',
		widget = forms.Textarea(
			attrs = {
				'class': 'form-control',
				'placeholder': 'Message...',
				'rows': 4,
		}),
	)