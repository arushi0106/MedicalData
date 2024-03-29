# Generated by Django 4.1.1 on 2022-11-22 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0012_alter_diseasedetails_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diseasedetails',
            name='modality',
            field=models.CharField(choices=[('X-ray', 'X-ray'), ('CT-scan', 'CT-scan'), ('MRI', 'MRI'), ('UltraSound', 'Ultrasound'), ('Angiography', 'Angiography'), ('Electrocardiogram', 'ECG'), ('PET', 'PET'), ('OCT', 'OCT')], default='X-ray', max_length=30),
        ),
        migrations.AlterField(
            model_name='patientprofile',
            name='blood_group',
            field=models.CharField(choices=[('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('AB+', 'AB+'), ('AB-', 'AB-'), ('O+', 'O+'), ('O-', 'O-')], default='A+', max_length=3),
        ),
    ]
