from django.urls import path
from . import views
app_name = "Home"
urlpatterns=[
	path('',views.home, name='home'),
	path('addgroup', views.addgroup, name = 'addgroup'),
	path('addgrouptodb', views.addgrouptodb, name = 'addgroouptodb'),
	path('send_email', views.send_email, name="send_email"),
	path('send_email_msg', views.send_email_msg, name = "send_email_msg")
]