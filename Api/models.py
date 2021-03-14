from django.db import models

# Create your models here.
class Master_Db(models.Model):
    Register_No = models.CharField(max_length=10,primary_key=True)
    Name = models.CharField(max_length=25)
    Room_No = models.CharField(max_length=10)
    Mobile_No = models.CharField(max_length=12)
    Parent_No = models.CharField(max_length=12)
    Email = models.CharField(max_length=20)
    Year = models.CharField(max_length=10)
    Department = models.CharField(max_length=10)
    Class = models.CharField(max_length=10)
    Father_Name = models.CharField(max_length=20)
    Gender = models.CharField(max_length=10)
    Date_of_birth = models.CharField(max_length=10)

    
class Login_Auth_Db(models.Model):
    Register_No = models.CharField(max_length=10,primary_key=True)
    Otp = models.CharField(max_length=10)

class Today_Attendance_Db(models.Model):
    Register_No = models.CharField(max_length=10,primary_key=True)
    Auth_Status = models.BooleanField()
    Auth_Time = models.CharField(max_length=20)
    Date = models.CharField(max_length=10) 
