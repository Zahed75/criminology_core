from django.urls import path
from main_app import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/',views.AboutSection,name='about'),
    path('course/',views.course,name='course'),
    path('facilites-details/<int:pk>/',views.faclities_details,name='facitlities-deatails'),
    path('teacher/',views.teacher,name='teacher'),
    path('teacher_details/<int:pk>/',views.DetailsTeacher,name='teacher_details'),
    path('course_details/<id>/',views.course_details,name='course_details'),
    path('event/',views.event,name='event'),
    path('event_details/<int:pk>/',views.details_event,name='event_details'),
    path('contact/',views.contact,name='contact'),
    path('blog/',views.blog,name='blog'),


]


# /*javascript:void(0);
