from django.contrib import messages
from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.views import generic
from django.views.generic.base import View
from django.contrib.auth.decorators import login_required
from .forms import ResearcherProfileForm, DoctorProfileForm, PatientProfileForm
from .models import *

# Create your views here.
def researcher_profile(request):
    if(ResearcherProfile.objects.filter(researcher=request.user).exists()):
        researcher = researcher = ResearcherProfile.objects.get(researcher=User.object.get(id=request.user.id))
        context = {
         'researcher': researcher
        }
        return render(request, 'researcher/profile.html', context)
    else:
        if request.method == 'POST':
            fm = ResearcherProfileForm(request.POST)
            if fm.is_valid():
                instance = fm.save(commit=False)
                instance.researcher = request.user
                print(instance.id)
                instance.save()
                messages.success(request, 'Your profile has been created')
                researcher = researcher = ResearcherProfile.objects.get(researcher=User.object.get(id=request.user.id))
                context = {
                'researcher': researcher
                    }

                return render(request, 'researcher/profile.html', context)
            else:
                messages.error(request, 'Please enter valid details')
                return render(request,'researcher/profile-form.html',{'form':fm})
        else:
                fm=ResearcherProfileForm()
                return render(request,'researcher/profile-form.html',{'form':fm})

def profile(request):
    if request.user.is_doctor == True :
        doctor = doctor = DoctorProfile.objects.get(doctor=User.object.get(id=request.user.id))
        context = {
            'doctor': doctor
        }

        return render(request, 'doctor/profile.html', context)
    elif request.user.is_researcher == True :
        researcher = researcher = ResearcherProfile.objects.get(researcher=User.object.get(id=request.user.id))
        context = {
            'researcher': researcher
        }

        return render(request, 'researcher/profile.html', context)
    else:
        print("NOT A Researcher!! and not a Doctor")
        return redirect('login')

def doctor_profile(request):
    if(DoctorProfile.objects.filter(doctor=request.user).exists()):
        dcotor = doctor = DoctorProfile.objects.get(doctor=User.object.get(id=request.user.id))
        context = {
         'doctor': doctor
        }
        return render(request, 'doctor/profile.html', context)
    else:
        if request.method == 'POST':
            fm = DoctorProfileForm(request.POST)
            if fm.is_valid():
                instance = fm.save(commit=False)
                instance.doctor = request.user
                print(instance.id)
                instance.save()
                messages.success(request, 'Your profile has been created')
                doctor = doctor = DoctorProfile.objects.get(doctor=User.object.get(id=request.user.id))
                context = {
                'doctor': doctor
                    }

                return render(request, 'doctor/profile.html', context)
            else:
                messages.error(request, 'Please enter valid details')
                return render(request,'doctor/profile-form.html',{'form':fm})
        else:
                fm=DoctorProfileForm()
                return render(request,'doctor/profile-form.html',{'form':fm})

def add_patient(request):
    if request.user.is_doctor == True : 
        if request.method == 'POST':
            fm = PatientProfileForm(request.POST)
            if fm.is_valid():
                instance = fm.save(commit=False)
                instance.added_by = request.user
                instance.save()
                messages.success(request,"Patient has been added successfully")
            else:
                messages.error(request,"Please enter valid details")
                return render(request,'doctor/patient-form.html',{'form':fm})
        else:
            fm = PatientProfileForm()
            return render(request,'doctor/patient-form.html',{'form':fm})
    else:
        messages.error(request,"You are not authorized to visit this")
        return redirect('login')


