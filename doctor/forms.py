from django import forms

from .models import *

class ResearcherProfileForm(forms.ModelForm):

    class Meta:
        model = ResearcherProfile

        fields = ['first_name', 'last_name', 'gender', 'phone', 'dob']