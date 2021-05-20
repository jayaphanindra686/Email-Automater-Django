from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from Home.models import Group_count

# Create your views here.

def login(request):
	user_name = request.POST['user_name']
	password = request.POST['password']
	user = auth.authenticate(username = user_name, password = password)
	if user is not None:
		auth.login(request, user)
		return redirect("Home/home")
	else:
		messages.info(request, "invalid credentials")
		return redirect("index.html")
	return render(request, 'index_1.html')
def register(request):
	return render(request, 'index_2.html')
def registered(request):
	first_name = request.POST['first_name']
	last_name = request.POST['last_name']
	user_name = request.POST['user_name']
	email = request.POST['email']
	password_1 = request.POST['password_1']
	password_2 = request.POST['password_2']
	if password_1 == password_2:
		if not User.objects.filter(username = user_name).exists():
			if not User.objects.filter(email = email).exists():
				user = User.objects.create_user(username = user_name, password = password_1, email = email, first_name = first_name, last_name = last_name)
				user.save()
				user = User.objects.filter(username = user_name)
				grp_count = Group_count.objects.create(USER_NAME = user_name, GRP_COUNT = 1 )
				grp_count.save()
				return redirect('/')
			else:
				messages.info(request, "EMAIL already registered")
				return redirect('register')
		else:
			messages.info(request, "User Name already taken")
			return redirect('register')
	else:
		print("Passwords didnot match")
		return render(request, 'index_2.html')
def addgroup(request):
	return render(request, "addgroup.html")
def addgrouptodb(request):
	home = emails()
	home.USER_NAME = user.username
	home.GRP_ID = 1
	home.EMAIL = email_1
	home.save()
	return render(request,"addgroup.html")