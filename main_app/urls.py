from django.urls import path
from main_app import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/',views.AboutSection,name='about'),
    # ==============================================
    path('facilites-details/<int:pk>/',views.faclities_details,name='facitlities-deatails'),
    # ===============================================
    path('teacher/',views.teacher,name='teacher'),
    path('teacher_details/<int:pk>/',views.DetailsTeacher,name='teacher_details'),
    # =====================================================
    path('course/',views.course,name='course'),
    path('course_details/<id>/',views.course_details,name='course_details'),
    # =====================================================
    path('event/',views.event,name='event'),
    path('event_details/<int:pk>/',views.details_event,name='event_details'),
    # ======================================================
    path('contact/',views.contact,name='contact'),
    path('research/',views.research,name='research'),
    path('research-details/<int:pk>/',views.research_details,name='research-details'),
    # =========================================================
    path('publication/',views.pub,name='publication'),
    path('details_pub/<int:pk>/',views.pub_details,name='details_pub')


]


# /*javascript:void(0);
