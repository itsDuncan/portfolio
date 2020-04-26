from django import forms
from .models import DesignJob, DesignCategory

class DesignJobForm1(forms.ModelForm):
	class Meta:
		model = DesignJob
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

class DesignJobForm2(forms.ModelForm):
	class Meta:
		model = DesignJob
		fields = ['category', 'description']

	category = forms.ModelChoiceField(
		queryset = DesignCategory.objects.all(),
		empty_label='Select design category',
		required = True,
		label = (''),
		widget = forms.Select(
			attrs = {
				'class':'form-control',
		}),
	)

	description = forms.CharField(
		required = True,
		label = '',
		widget = forms.Textarea(
			attrs = {
			'class': 'form-control',
			'placeholder': 'How best can you explain your aspired design',
		}),
	)