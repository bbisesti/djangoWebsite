# Generated by Django 2.0.4 on 2018-04-13 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contactForm', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactform',
            name='message',
            field=models.TextField(default=''),
        ),
    ]
