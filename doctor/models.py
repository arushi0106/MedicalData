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