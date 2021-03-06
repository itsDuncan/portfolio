# Generated by Django 3.0.5 on 2020-04-23 07:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hirewebdev',
            name='slug',
            field=models.SlugField(default=django.utils.timezone.now, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='hirewebdev',
            name='project_description',
            field=models.TextField(),
        ),
    ]
