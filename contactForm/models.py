# Database Models
from django.db import models

# validation
from django.core.validators import validate_email

# django utilities
from django.utils import timezone

# Create your models here.

HELP_TYPE = (
	('Help', 'Help'),
	('Bug Report', 'Bug Report'),
	('Just Saying Hi!', 'Just Saying Hi!'),
	('Request Access', 'Request Access')
)


class ContactForm(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	middle_name = models.CharField(max_length=50, blank=True)
	cell_phone = models.CharField(max_length=20)
	home_phone = models.CharField(max_length=20,blank=True)
	email = models.CharField(max_length=50, validators=[validate_email])
	message = models.TextField(blank=False,default='')
	help_type = models.CharField(max_length=20, choices=HELP_TYPE, blank=False, default='Help')
	created_date = models.DateTimeField(default=timezone.now)