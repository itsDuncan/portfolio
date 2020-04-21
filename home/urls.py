from django.urls import re_path
from . import views
from .views import HireDevWizard 

app_name = 'home'

urlpatterns = [
	re_path(r'^$', views.home),
	re_path(r'^home/$', views.home, name='landing-page'),
	re_path(r'^contact/$', views.contact, name='contact'),
	# re_path(r'^hire/web-development/$', views.hire_dev, name='hire-dev'),
	re_path(r'^hire/graphic-design/$', views.hire_designer, name='hire-designer'),
	re_path(r'^hire/web-development/$', HireDevWizard.as_view(), name='hire-wizard'),
]