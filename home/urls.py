from django.urls import re_path
from . import views

app_name = 'home'

urlpatterns = [
	re_path(r'^$', views.home),
	re_path(r'^home/$', views.home, name='landing-page'),
	re_path(r'^contact/$', views.contact, name='contact'),
]