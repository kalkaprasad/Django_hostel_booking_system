from django.db import models
from django.db.models import ImageField


class Employee(models.Model): # django provide built in  the models
    # model is our database tables ..
    eid=models.CharField(max_length=20)
    ename=models.CharField(max_length=50)
    eemail=models.EmailField()
    econtact=models.CharField(max_length=20)

    # Meta class is a Instance Class / it is Alawyes Global../ it also called sub class
    class Meta: # it have more importance..
        db_table="employee"

        # this is use for create the Tables...

# django give us prebuild form html format..



class useraccount(models.Model):
    id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=30)
    email=models.EmailField()
    phone=models.CharField(max_length=20)
    password=models.CharField(max_length=20)

    # now we need us a meta Class
    class Meta:
        db_table="useraccount"


class upload_data(models.Model): # this is the model
    id = models.IntegerField(primary_key=True)
    files=models.CharField(max_length=200)
    hostelname=models.CharField(max_length=50)
    hostelad=models.CharField(max_length=100)
    hosterate=models.CharField(max_length=20)
    hosteldes=models.CharField(max_length=100)

    class Meta:
        db_table="upload" # this is the our Table Name of the data base..


class bookservice(models.Model):
    id=models.AutoField(primary_key=True)
    cname = models.CharField(max_length=50)
    cphone = models.CharField(max_length=12)
    cemail = models.EmailField()
    caddress = models.CharField(max_length=60)
    ctime = models.CharField(max_length=30)
    class Meta:
        db_table = "bookservice"




class mylogin(models.Model):
    id=models.AutoField(primary_key=True)
    email=models.EmailField()
    password=models.CharField(max_length=30)

    class Meta:
        db_table="mylogin"







