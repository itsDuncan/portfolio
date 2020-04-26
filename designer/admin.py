from django.contrib import admin
from .models import DesignJob, DesignCategory

admin.site.register(DesignCategory)
admin.site.register(DesignJob)