from django.urls import path,include
from doctor import views

urlpatterns = [

    path('add_patient',views.add_patient,name="add_patient"),
    path('show_patient',views.show_patient,name="show_patient"),
    path('profile_researcher', views.researcher_profile, name="profile_researcher"),
    path('profile_doctor', views.doctor_profile, name="profile_doctor"),
    path('add_disease', views.add_disease, name='add_disease'),
    path('user_profile', views.profile, name="profile_user"),
    path('show_disease', views.show_disease, name="show_disease"),
    # path('unit_student/<int:bid>',views.units,name="unit_student"),
    # path('giveRating/<int:bid>',views.giveRating,name="giveRating"),
]