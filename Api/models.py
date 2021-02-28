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
    Genter = models.CharField(max_length=10)
    Date_of_birth = models.CharField(max_length=10)
    