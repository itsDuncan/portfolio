from django import forms
from .validators import ascii_validator, email_validator
from django.core.validators import RegexValidator, EmailValidator

class ContactForm(forms.Form):
	senders_name = forms.CharField(
		required = True,
		label = (''),
		widget = forms.TextInput(
			attrs = {
				'class':'form-control',
				'placeholder': 'Your Name',
		}),
	)

	senders_email = forms.EmailField(
		required = True,
		label = (''),
		widget = forms.TextInput(
			attrs = {
				'class': 'form-control',
				'placeholder': 'Your Email',
		}),
	)

	message = forms.CharField(
		required = True,
		label = (''),
		widget = forms.Textarea(
			attrs = {
				'class': 'form-control',
				'placeholder': 'Message...',
				'rows': 4,
		}),
	)

class TrackProjectForm(forms.Form):
	project_name = forms.CharField(
		required = True,
		label = (''),
		widget = forms.TextInput(
			attrs = {
				'class':'form-control',
				'placeholder': 'Project Name',
		}),
	)