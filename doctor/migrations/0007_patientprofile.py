# Generated by Django 4.1.1 on 2022-10-29 08:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('doctor', '0006_alter_doctorprofile_verified_admin'),
    ]

    operations = [
        migrations.CreateModel(
            name='PatientProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(choices=[('M', 'MALE'), ('F', 'FEMALE')], default='M', max_length=1)),
                ('first_name', models.CharField(max_length=255)),
                ('blood_group', models.CharField(max_length=255)),
                ('hospital', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('phone', models.IntegerField()),
                ('dob', models.DateField()),
                ('added_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
