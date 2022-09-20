from django.contrib import admin
from .models import *


# Register your models here.



@admin.register(Home)
class HomeAdmin(admin.ModelAdmin):
    list_display= ('heading', 'sub_heading')



@admin.register(Facilites)
class FacilitesiAdmin(admin.ModelAdmin):
    list_display= ('title', 'image','created')


@admin.register(FacilitiesDetails)
class FacilitiesDetails(admin.ModelAdmin):
    list_display=('title','descriptions','teacher_name','fb_link','twitter_link')


@admin.register(TeacherSection)
class TeacherSectionAdmin(admin.ModelAdmin):
    list_display = ('teacher_name', 'TeacherDesignations', 'TeacherImage')


@admin.register(ChairmanSection)
class ChairmanSectionAdmin(admin.ModelAdmin):
    list_display= ('chairman_name', 'welcome_message', 'chairman_image')


@admin.register(about)
class aboutAdmin(admin.ModelAdmin):
    list_display=('about_description','about_image')



@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display=('event_title','event_date','event_time','event_image')



@admin.register(EventDetails)
class EventDetailsAdmin(admin.ModelAdmin):
    list_display=('event_title','event_descriptions','event_pdf','event_main_speaker')



@admin.register(TeacherDetail)
class TeacherDetailAdmin(admin.ModelAdmin):
    list_display=('id','teacher_name')


@admin.register(Publications)
class PublicationsAdmin(admin.ModelAdmin):
    list_display=('id','title','descriptions','image')

@admin.register(PublicationDetail)
class PublicationDetailAdmin(admin.ModelAdmin):
    list_display=('id','title','author_name')


@admin.register(Research)
class ResearchAdmin(admin.ModelAdmin):
    list_display=('id','title','image','publish_date')


@admin.register(ResearchDetail)
class ResearchDetailAdmin(admin.ModelAdmin):
    list_display=('id','title','author_name')
