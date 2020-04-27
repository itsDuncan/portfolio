from django.urls import re_path
from . import views
from .views import DeveloperJobWizard, DeveloperJobDetailView

app_name = 'developer'

urlpatterns = [
	re_path(r'^hire/$', DeveloperJobWizard.as_view(), name='hire'),
	re_path(r'^active-projects/(?P<slug>[\w-]+)', DeveloperJobDetailView.as_view(), name='project-detail'),
]