from django.urls import path,include
from doctor import views

urlpatterns = [

    path('add_patient',views.add_patient,name="add_patient"),
    path('show_patient',views.show_patient,name="show_patient"),
    path('profile_researcher', views.researcher_profile, name="profile_researcher"),
    path('profile_doctor', views.doctor_profile, name="profile_doctor"),
    path('add_disease_patient/<str:id>', views.add_disease_patient, name='add_disease_patient'),
    path('user_profile', views.profile, name="profile_user"),
    path('show_disease', views.show_disease, name="show_disease"),
    path('show_patient_details/<str:id>', views.show_patient_details, name="show_patient_details"),

]