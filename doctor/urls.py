from django.urls import path,include
from doctor import views

urlpatterns = [

    path('add_patient',views.add_patient,name="add_patient"),
    path('profile_researcher', views.researcher_profile, name="profile_researcher"),
    path('profile_doctor', views.doctor_profile, name="profile_doctor"),
    # path('student_dash', views.dash, name='StudentDash'),
    path('user_profile', views.profile, name="profile_user"),
    # path('unit_student/<int:bid>',views.units,name="unit_student"),
    # path('giveRating/<int:bid>',views.giveRating,name="giveRating"),
]