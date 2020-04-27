from django.urls import re_path
from . import views
from .views import DesignJobWizard

app_name = 'designer'

urlpatterns = [
	re_path(r'^hire/$', DesignJobWizard.as_view(), name='hire'),
]