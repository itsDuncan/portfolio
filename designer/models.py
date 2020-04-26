from django.db import models
from .utils import unique_slug_generator, unique_slug_category_generator
from django.db.models.signals import pre_save
from django.dispatch import receiver

class DesignCategory(models.Model):
	slug = models.SlugField(unique=True)
	category = models.CharField(max_length=50)

	def __str__(self):
		return "{}".format(self.category)

class DesignJob(models.Model):
	slug = models.SlugField(unique=True)
	senders_name = models.CharField(max_length=50)
	senders_email = models.EmailField(max_length=50)
	category = models.ForeignKey(DesignCategory, related_name='design_category', on_delete=models.SET_NULL, blank=True, null=True)
	description = models.TextField()
	additional_info = models.TextField()
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	def __str__(self):
		return "{}".format(self.senders_name)

@receiver(pre_save, sender=DesignJob)
def design_job_presave_receiver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = unique_slug_generator(instance)

@receiver(pre_save, sender=DesignCategory)
def design_category_presave_receiver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = unique_slug_category_generator(instance)