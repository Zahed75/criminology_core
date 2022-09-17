from django.contrib import admin
from .models import *


# Register your models here.



@admin.register(Home)
class HomeAdmin(admin.ModelAdmin):
    list_display= ('heading', 'sub_heading')

@admin.register(Welcome)
class WelcomeAdmin(admin.ModelAdmin):
    list_display= ('descriptions',)

@admin.register(Facilites)
class FacilitesiAdmin(admin.ModelAdmin):
    list_display= ('title', 'image','created')


@admin.register(FacilitiesDetails)
class FacilitiesDetails(admin.ModelAdmin):
    list_display=('title','descriptions','teacher_name','fb_link','twitter_link')


@admin.register(TeacherSection)
class TeacherSectionAdmin(admin.ModelAdmin):
    list_display = ('TeacherName', 'TeacherDesignations', 'TeacherImage')


@admin.register(ChairmanSection)
class ChairmanSectionAdmin(admin.ModelAdmin):
    list_display= ('chairman_name', 'welcome_message', 'chairman_image')


@admin.register(about)
class aboutAdmin(admin.ModelAdmin):
    list_display=('title','about_description','about_image')



@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display=('event_title','event_date','event_time')



@admin.register(EventDetails)
class EventDetailsAdmin(admin.ModelAdmin):
    list_display=('title','event_descriptions','event_pdf')
