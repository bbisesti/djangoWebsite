from django.urls import path

from . import views

app_name = 'contactForm'
urlpatterns = [
	path('', views.index, name='index'),
	path('submitted/', views.submitted, name='submitted')
]