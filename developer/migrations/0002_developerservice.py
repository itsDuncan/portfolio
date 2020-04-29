# Generated by Django 3.0.5 on 2020-04-29 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('developer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeveloperService',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(unique=True)),
                ('service_name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('cost', models.CharField(max_length=50)),
            ],
        ),
    ]
