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

class WebDevHireForm1(forms.Form):
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

class WebDevHireForm2(forms.Form):
	project_name = forms.CharField(
		required = True,
		label = (''),
		widget = forms.TextInput(
			attrs = {
				'class':'form-control',
				'placeholder': 'Project/Website Name',
		}),
	)

	project_description = forms.CharField(
		required = True,
		label = '',
		widget = forms.Textarea(
			attrs = {
			'class': 'form-control',
			'placeholder': 'How best can you explain the website',
		}),
	)

class WebDevHireForm3(forms.Form):
	ui_design = forms.BooleanField(
		required = False,
		widget = forms.CheckboxInput(
			attrs = {
			}),
		)

	design_documentation = forms.BooleanField(
		required = False,
		widget = forms.CheckboxInput(
			attrs = {
			}),
		)

	favicon = forms.BooleanField(
		required = False,
		widget = forms.CheckboxInput(
			attrs = {
			}),
		)

	branding = forms.BooleanField(
		required = False,
		widget = forms.CheckboxInput(
			attrs = {
			}),
		)

class WebDevHireForm4(forms.Form):
	custom_domain = forms.BooleanField(
		required = False,
		widget = forms.CheckboxInput(
			attrs = {
			}),
		)

	web_hosting = forms.BooleanField(
		required = False,
		widget = forms.CheckboxInput(
			attrs = {
			}),
		)

	storage_database = forms.BooleanField(
		required = False,
		widget = forms.CheckboxInput(
			attrs = {
			}),
		)

	transactional_emails = forms.BooleanField(
		required = False,
		widget = forms.CheckboxInput(
			attrs = {
			}),
		)

	admin_panel = forms.BooleanField(
		required = False,
		widget = forms.CheckboxInput(
			attrs = {
			}),
		)

	responsiveness = forms.BooleanField(
		required = False,
		widget = forms.CheckboxInput(
			attrs = {
			}),
		)

	payment_config = forms.BooleanField(
		required = False,
		widget = forms.CheckboxInput(
			attrs = {
			}),
		)

class WebDevHireForm5(forms.Form):
	seo = forms.BooleanField(
		required = False,
		widget = forms.CheckboxInput(
			attrs = {
			}),
		)

	google_analytics = forms.BooleanField(
		required = False,
		widget = forms.CheckboxInput(
			attrs = {
			}),
		)

	blog = forms.BooleanField(
		required = False,
		widget = forms.CheckboxInput(
			attrs = {
			}),
		)

	social_acc_integration = forms.BooleanField(
		required = False,
		widget = forms.CheckboxInput(
			attrs = {
			}),
		)

	perfective_features = forms.BooleanField(
		required = False,
		widget = forms.CheckboxInput(
			attrs = {
			}),
		)

class WebDevHireForm6(forms.Form):
	domain_security = forms.BooleanField(
		required = False,
		widget = forms.CheckboxInput(
			attrs = {
			}),
		)

	app_security = forms.BooleanField(
		required = False,
		widget = forms.CheckboxInput(
			attrs = {
			}),
		)

	privacy_policy = forms.BooleanField(
		required = False,
		widget = forms.CheckboxInput(
			attrs = {
			}),
		)

	terms_and_conditions = forms.BooleanField(
		required = False,
		widget = forms.CheckboxInput(
			attrs = {
			}),
		)

	additional_features = forms.CharField(
		required = False,
		widget = forms.Textarea(
			attrs = {
				'class': 'form-control',
				'placeholder': 'Additional Features...',
				'rows': 4,
			}),
		)