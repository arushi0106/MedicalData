from django.contrib import messages
from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.views import generic
from django.views.generic.base import View
from django.contrib.auth.decorators import login_required
from .forms import ResearcherProfileForm
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
    if request.user.is_researcher == True :
        researcher = researcher = ResearcherProfile.objects.get(researcher=User.object.get(id=request.user.id))
        context = {
            'researcher': researcher
        }

        return render(request, 'researcher/profile.html', context)
    else:
        print("NOT A Researcher!!")
        return redirect('login')