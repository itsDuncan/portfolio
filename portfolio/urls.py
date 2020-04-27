from django.contrib import admin
from django.urls import path, re_path, include

urlpatterns = [
    path('dun-admin/', admin.site.urls),
    re_path(r'', include('home.urls')),
    re_path(r'^designer/', include('designer.urls')),
    re_path(r'^developer/', include('developer.urls')),
]