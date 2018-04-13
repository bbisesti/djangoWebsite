from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse

from .forms import ContactForm

# logging
import logging

logger = logging.getLogger(__name__)

# Create your views here.


def index(request):

	if request.method == "POST":
		form = ContactForm(request.POST)
		if form.is_valid():
			form.save()
			context = {
				'message': 'Form Saved Successfully',
				'nbar': 'Contact'
			}
			return HttpResponseRedirect(reverse('contactForm:submitted'), context)
	else:
		form = ContactForm()
	context = {
		'form': form,
		'nbar': 'Contact'
	}
	return render(request, 'contactForm/index.html', context)


def submitted(request):
	context = {
		'nbar': 'Contact'
	}
	return render(request, 'contactForm/submitted.html', context)
