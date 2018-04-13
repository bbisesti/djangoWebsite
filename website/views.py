from django.shortcuts import get_object_or_404, render, redirect
from django.http import JsonResponse

# Authentication
from django.contrib.auth import authenticate, login

# models
from django.apps import apps
from django.db.models import Count

contactForm = apps.get_model('contactForm', 'ContactForm')

# Create your views here.


def index(request):
	context = {
		'nbar': 'Home'
	}
	return render(request, 'index.html', context)


def results(request):
	context = {
		'nbar': 'Results'
	}
	return render(request, 'results.html', context)


def data(request):
	data = contactForm.objects.values('help_type').annotate(values=Count('first_name'))
	return JsonResponse({'data': list(data)})

def user(request):
	data = contactForm.objects.values('first_name').annotate(values=Count('first_name'))
	return JsonResponse({'data': list(data)})