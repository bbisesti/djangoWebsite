# Forms
from django import forms

# models
from .models import ContactForm

# Validation
from django.core.validators import validate_email


class ContactForm(forms.ModelForm):

	class Meta:
		model = ContactForm
		fields = ('first_name', 'middle_name', 'last_name', 'cell_phone', 'home_phone', 'email', 'help_type', 'message')