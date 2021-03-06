# Generated by Django 2.0.4 on 2018-04-13 16:23

import django.core.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('middle_name', models.CharField(blank=True, max_length=50)),
                ('cell_phone', models.CharField(max_length=20)),
                ('home_phone', models.CharField(blank=True, max_length=20)),
                ('email', models.CharField(max_length=50, validators=[django.core.validators.EmailValidator()])),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
