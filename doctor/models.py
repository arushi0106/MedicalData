from django.db import models
from account.models import *
import os 
import uuid
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


def get_upload_path(instance, filename):
    ext = filename.split('.')[-1]
    # get filename
    if instance.pk:
        filename = '{}.{}'.format(instance.pk, ext)
    else:
        filename = "%s.%s" % (uuid.uuid4(), ext)
        # filename= instance.name + instance.modality + uuid.uuid4()
    return os.path.join(
      "%s" % instance.name, "%s" % instance.modality, filename)

Possibility = (
("YES", "YES"),
("NO", "NO"),
)

TypeofModality = (
    ("X-ray","X-ray"),
    ("CT-scan","CT-scan"),
    ("MRI","MRI"),
    ("UltraSound","Ultrasound")
)

class DiseaseDetails(models.Model):
    patient = models.ForeignKey(PatientProfile,on_delete=models.CASCADE)
    name = models.CharField(max_length=30,null=True)
    modality=models.CharField(max_length=30,choices=TypeofModality,default='X-ray')
    diagonised = models.CharField(max_length = 20, choices = Possibility, default = 'YES')
    img=models.ImageField(upload_to=get_upload_path,null=True)
    # img=models.ImageField(null=True)

    def __str__(self):
        return self.name

