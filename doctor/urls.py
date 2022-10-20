from django.urls import path,include
from doctor import views

urlpatterns = [

    # path('home_student',views.home_student,name="home_student"),
    path('profile_researcher', views.researcher_profile, name="profile_researcher"),
    # path('student_dash', views.dash, name='StudentDash'),
    path('researcher_profile', views.profile, name="ResearcherProfile"),
    # path('unit_student/<int:bid>',views.units,name="unit_student"),
    # path('giveRating/<int:bid>',views.giveRating,name="giveRating"),
]