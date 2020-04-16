from django.urls import re_path
from . import views

app_name = 'home'

urlpatterns = [
	re_path('', views.home, name='landing-page'),
]