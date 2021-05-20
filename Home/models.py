from django.db import models

# Create your models here.

class All_Emails(models.Model):
	USER_NAME = models.CharField(max_length = 50)
	EMAIL = models.CharField(max_length = 50)
	GRP_ID = models.IntegerField()
	GRP_NAME = models.CharField(max_length = 50)
class All_Group_count(models.Model):
	USER_NAME = models.CharField(max_length=50)
	GRP_COUNT = models.IntegerField()

class Emails(models.Model):
	USER_NAME = models.CharField(max_length = 50)
	EMAIL = models.CharField(max_length = 50)
	GRP_ID = models.IntegerField()
	GRP_NAME = models.CharField(max_length = 50)
class Group_count(models.Model):
	USER_NAME = models.CharField(max_length=50)
	GRP_COUNT = models.IntegerField()
class grp:
	grp_name : str
	email_list = list
