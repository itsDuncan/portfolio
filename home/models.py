from django.db import models
from .utils import unique_slug_generator
from django.db.models.signals import pre_save
from django.dispatch import receiver

class HireWebDev(models.Model):
	slug = models.SlugField(unique=True)
	senders_name = models.CharField(max_length=50)
	senders_email = models.EmailField(max_length=50)
	project_name = models.CharField(max_length=50)
	project_description = models.TextField()
	ui_design = models.BooleanField(default=True)
	design_documentation = models.BooleanField(default=False)
	favicon = models.BooleanField(default=False)
	branding = models.BooleanField(default=False)
	custom_domain = models.BooleanField(default=True)
	web_hosting = models.BooleanField(default=False)
	storage_database = models.BooleanField(default=True)
	transactional_emails = models.BooleanField(default=False)
	admin_panel = models.BooleanField(default=False)
	responsiveness = models.BooleanField(default=False)
	payment_config = models.BooleanField(default=False)
	seo = models.BooleanField(default=False)
	google_analytics = models.BooleanField(default=False)
	blog = models.BooleanField(default=False)
	social_acc_integration = models.BooleanField(default=False)
	perfective_features = models.BooleanField(default=False)
	domain_security = models.BooleanField(default=False)
	app_security = models.BooleanField(default=False)
	privacy_policy = models.BooleanField(default=False)
	terms_and_conditions = models.BooleanField(default=False)
	additional_features = models.CharField(max_length=255)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	def __str__(self):
		return "{} - {}".format(self.senders_name, self.project_name)

@receiver(pre_save, sender=HireWebDev)
def web_dev_presave_receiver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = unique_slug_generator(instance)