from django.db import models
from account.models import *
# Create your models here.

class ResearcherProfile(models.Model):
    GENDER = (('M','MALE'),('F','FEMALE'))
    researcher = models.OneToOneField(User,on_delete=models.CASCADE)
    gender = models.CharField(default='M',choices=GENDER, max_length=1)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone = models.IntegerField()
    dob = models.DateField()

    def __str__(self):
        return self.first_name

class DoctorProfile(models.Model):
    GENDER = (('M','MALE'),('F','FEMALE'))
    doctor = models.OneToOneField(User,on_delete=models.CASCADE)
    gender = models.CharField(default='M',choices=GENDER, max_length=1)
    first_name = models.CharField(max_length=255)
    license_key = models.CharField(max_length=255)
    verified_admin = models.BooleanField(default=False,null=True)
    last_name = models.CharField(max_length=255)
    phone = models.IntegerField()
    dob = models.DateField()

    def __str__(self):
        return self.first_name

class PatientProfile(models.Model):
    GENDER = (('M','MALE'),('F','FEMALE'))
    added_by = models.ForeignKey(User,on_delete=models.CASCADE)
    gender = models.CharField(default='M',choices=GENDER, max_length=1)
    first_name = models.CharField(max_length=255)
    blood_group = models.CharField(max_length=255)
    hospital = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone = models.IntegerField()
    dob = models.DateField()

    def __str__(self):
        return self.first_name