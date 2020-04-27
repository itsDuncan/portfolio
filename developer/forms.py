from django import forms
from .models import DeveloperJob

class DeveloperJobForm1(forms.ModelForm):
	class Meta:
		model = DeveloperJob
		fields = ['senders_name', 'senders_email']

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

class DeveloperJobForm2(forms.ModelForm):
	class Meta:
		model = DeveloperJob
		fields = ['project_name', 'project_description']

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

class DeveloperJobForm3(forms.ModelForm):
	class Meta:
		model = DeveloperJob
		fields = ['ui_design', 'design_documentation', 'favicon', 'branding']

	ui_design = forms.BooleanField(
		required = False,
		widget = forms.CheckboxInput(
			attrs = {
				'class': 'form-control',
				'title': 'This is required for all websites',
				'checked': 'checked',
			}),
		label = 'User Interface Design',
		)

	design_documentation = forms.BooleanField(
		required = False,
		widget = forms.CheckboxInput(
			attrs = {
				'class': 'form-control',
			}),
		label = 'Design Documentation',
		)

	favicon = forms.BooleanField(
		required = False,
		widget = forms.CheckboxInput(
			attrs = {
				'class': 'form-control',
			}),
		label = 'Favicon',
		)

	branding = forms.BooleanField(
		required = False,
		widget = forms.CheckboxInput(
			attrs = {
				'class': 'form-control',
			}),
		label = 'Branding',
		)

class DeveloperJobForm4(forms.Form):
	class Meta:
		model = DeveloperJob
		fields = ['custom_domain', 'web_hosting', 'storage_database', 'transactional_emails', 'admin_panel', 'responsiveness', 'payment_config']

	custom_domain = forms.BooleanField(
		required = False,
		widget = forms.CheckboxInput(
			attrs = {
				'class': 'form-control',
			}),
		label = 'Custom Domain',
		)

	web_hosting = forms.BooleanField(
		required = False,
		widget = forms.CheckboxInput(
			attrs = {
				'class': 'form-control',
			}),
		label = 'Web Hosting',
		)

	storage_database = forms.BooleanField(
		required = False,
		widget = forms.CheckboxInput(
			attrs = {
				'class': 'form-control',
			}),
		label = 'Storage Database',
		)

	transactional_emails = forms.BooleanField(
		required = False,
		widget = forms.CheckboxInput(
			attrs = {
				'class': 'form-control',
			}),
		label = 'Transactional Emails',
		)

	admin_panel = forms.BooleanField(
		required = False,
		widget = forms.CheckboxInput(
			attrs = {
				'class': 'form-control',
			}),
		label = 'Admin Panel',
		)

	responsiveness = forms.BooleanField(
		required = False,
		widget = forms.CheckboxInput(
			attrs = {
				'class': 'form-control',
			}),
		label = 'Responsiveness',
		)

	payment_config = forms.BooleanField(
		required = False,
		widget = forms.CheckboxInput(
			attrs = {
			}),
		label = 'Payment Configuration',
		)

class DeveloperJobForm5(forms.Form):
	class Meta:
		model = DeveloperJob
		fields = ['seo', 'google_analytics', 'blog', 'social_acc_integration', 'perfective_features']

	seo = forms.BooleanField(
		required = False,
		widget = forms.CheckboxInput(
			attrs = {
				'class': 'form-control',
			}),
		label = 'Search Engine Optimization',
		)

	google_analytics = forms.BooleanField(
		required = False,
		widget = forms.CheckboxInput(
			attrs = {
				'class': 'form-control',
			}),
		label = 'Google Analytics',
		)

	blog = forms.BooleanField(
		required = False,
		widget = forms.CheckboxInput(
			attrs = {
				'class': 'form-control',
			}),
		label = 'Blog',
		)

	social_acc_integration = forms.BooleanField(
		required = False,
		widget = forms.CheckboxInput(
			attrs = {
				'class': 'form-control',
			}),
		label = 'Social Accounts Integration'
		)

	perfective_features = forms.BooleanField(
		required = False,
		widget = forms.CheckboxInput(
			attrs = {
				'class': 'form-control',
			}),
		label = 'Perfective Features',
		)

class DeveloperJobForm6(forms.Form):
	class Meta:
		model = DeveloperJob
		fields = ['domain_security', 'app_security', 'privacy_policy', 'terms_and_conditions', 'additional_features']

	domain_security = forms.BooleanField(
		required = False,
		widget = forms.CheckboxInput(
			attrs = {
				'class': 'form-control',
			}),
		label = 'Domain Security',
		)

	app_security = forms.BooleanField(
		required = False,
		widget = forms.CheckboxInput(
			attrs = {
				'class': 'form-control',
			}),
		label = 'Application Security',
		)

	privacy_policy = forms.BooleanField(
		required = False,
		widget = forms.CheckboxInput(
			attrs = {
				'class': 'form-control',
			}),
		label = 'Privacy Policy',
		)

	terms_and_conditions = forms.BooleanField(
		required = False,
		widget = forms.CheckboxInput(
			attrs = {
				'class': 'form-control',
			}),
		label = 'Terms and Conditions'
		)

	additional_features = forms.CharField(
		required = False,
		widget = forms.Textarea(
			attrs = {
				'class': 'form-control',
				'placeholder': 'Additional Features...',
				'rows': 4,
			}),
		label = ''
		)