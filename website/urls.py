from django.urls import include, path

from . import views

app_name = 'website'
urlpatterns = [
	path('', views.index, name='index'),
	path('results', views.results, name='results'),
	path('accounts/', include('django.contrib.auth.urls')),
	path('data/', views.data, name='data'),
	path('user/', views.user, name='user')
]