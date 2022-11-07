import django_filters

from .models import *

class DiseaseFilter(django_filters.FilterSet):
    class Meta:
        model = DiseaseDetails
        fields = ['patient','name','modality']