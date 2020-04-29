from django.contrib import admin
from .models import DeveloperJob, DeveloperService

admin.site.register(DeveloperJob)
admin.site.register(DeveloperService)