from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.core.mail import EmailMessage
from .models import Emails, Group_count, grp
# Create your views here.
userr = None
di = {}
def index(request):
	return render(request, 'index.html')
def home(request):
	if request.method!='POST':
		return render(request, "home.html")
	global userr
	user_name = request.POST['user_name']
	password = request.POST['password']
	user = auth.authenticate(username = user_name, password = password)
	if user is not None:
		userr = user
		auth.login(request, user)
		print(user)
		user1 = Emails.objects.filter(USER_NAME = user_name).order_by('GRP_ID')
		print(user1.__dict__)
		for email in user1:
			print(email.GRP_NAME)
		#print(user1)
		count = 1
		global di
		for email in user1:
			if email.GRP_NAME not in di:
				di[email.GRP_NAME] = []
			di[email.GRP_NAME].append(email)
		print(di)
		li = []
		count=-1
		for key,value in di.items():
			li.append(key)
			li.append([])
			count+=2
			for i in value:
				li[count].append(i)
		return render(request, "home.html",{'emails':li})
	else:
		messages.info(request, "invalid credentials")
		return redirect("index.html")
	return render(request, 'index_1.html')
def addgroup(request):
	return render(request, "addgroup.html")
def addgrouptodb(request):
	print(request.POST)
	for i in range(0,1001):
		print("hhi",i)
		if request.POST.__contains__('email_'+str(i)):
			print('email_'+str(i))
			home = Emails()
			home.USER_NAME = userr.username
			home.GRP_ID = 2
			home.GRP_NAME = request.POST['grpname']
			home.EMAIL = request.POST['email_'+str(i)]
			home.save()
		else:
			break
	grp_count = Group_count.objects.get(USER_NAME = userr.username)
	#print(grp_count.USER_NAME)
	print(grp_count.__dict__)
	count = grp_count.GRP_COUNT
	print(count)
	Group_count.objects.filter(USER_NAME = userr.username).update(GRP_COUNT=count+1)
	
	return redirect("Home:home")
def send_email(request):
		grp_name = request.POST["grp_name"]
		obj=grp()
		obj.grp_name = grp_name
		#obj.email_list = di[grp_name]
		di1 = di[grp_name]
		li = [len(di1), "email_0"]
		count=0
		for i in di1:
			count+=1
			li.append(i)
			li.append("email_"+str(count))
		print(li)
		obj.email_list = li
		return render(request, "send_email.html",{"grp":obj })
def send_email_msg(request):
	print()
	print()
	print()
	global di1
	email_count = len(request.POST)-2
	di = request.POST.dict()
	no_of_emails = int(request.POST['email_count'])
	print(di)
	i=0
	count=-1
	di2 = {}
	print()
	print()
	print()
	for key, value in di.items():
		if count==-1 or count==0 or count==1:
			count+=1
			continue
		elif count % 2 == 0:
			val = value
		else:
			di2[key] = [value,val]
		count+=1
	print(di2)
	print(no_of_emails)
	li=[]
	for i in range(1,no_of_emails+1):
		if "email_"+str(i) in di2:
			try:
				print("email_"+str(i))
				print(
			
					di2["email_"+str(i)][0],
					"jayaphanindra4@gmail.com",
					[di2["email_"+str(i)][1]])
				k = EmailMessage(
					"",
					di2["email_"+str(i)][0],
					"18501A0546@pvpsiddhartha.ac.in",
					[di2["email_"+str(i)][1]]
				)
				k.send()
			except:
				print("could not send mail to this address")
				li.append("Email not sent to "+ str(di2["email_"+str(i)]))

			print("Good Morning")
		if len(li)==0:
			li=["Emails sent Sucessfully"]
	return render(request, "successful.html", {"lists":li})
