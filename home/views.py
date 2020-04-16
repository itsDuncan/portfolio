from django.shortcuts import render

def home(request):
	template_name = 'home/home.html'
	context = {}

	return render(request, template_name, context)

def contact(request):
	template_name = 'home/contact.html'
	context = {}

	return render(request, template_name, context)