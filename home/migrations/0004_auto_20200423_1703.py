# Generated by Django 3.0.5 on 2020-04-23 14:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20200423_1653'),
    ]

    operations = [
        migrations.AddField(
            model_name='hirewebdev',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hirewebdev',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
