from django.contrib import admin
from .models import *


# Register your models here.



@admin.register(Home)
class HomeAdmin(admin.ModelAdmin):
    list_display= ('heading', 'sub_heading')

@admin.register(Welcome)
class WelcomeAdmin(admin.ModelAdmin):
    list_display= ('heading', 'desricptions')

@admin.register(Facilites)
class FacilitesiAdmin(admin.ModelAdmin):
    list_display= ('title', 'image','created')




@admin.register(TeacherSection)
class TeacherSectionAdmin(admin.ModelAdmin):
    list_display = ('TeacherName', 'TeacherDesignations', 'TeacherImage')


@admin.register(WelcomeSection)
class WelcomeSectionAdmin(admin.ModelAdmin):
    list_display= ('chairman_name', 'welcome_message', 'chairman_image')
