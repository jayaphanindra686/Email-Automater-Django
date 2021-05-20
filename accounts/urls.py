from django.urls import path
from . import views
urlpatterns=[
	path('login',views.login, name='login'),
	path('register', views.register, name = 'register'),
	path('registered', views.registered, name = 'registered'),
	path('addgroup', views.addgroup, name = 'addgroup'),
	path('addgrouptodb', views.addgrouptodb, name = "addgrouptodb")
]