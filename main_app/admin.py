from django.contrib import admin
from .models import *


# Register your models here.

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('course_title', 'course_image',
                    'course_duration', 'class_size', 'class_durations', 'course_descriptions')


@admin.register(CourseDetail)
class CourseDetailAdmin(admin.ModelAdmin):
    list_display = ('course_instructor', 'instructor_fb', 'instructor_twitter')


@admin.register(TeacherSection)
class TeacherSectionAdmin(admin.ModelAdmin):
    list_display = ('TeacherName', 'TeacherDesignations', 'TeacherImage')


@admin.register(WelcomeSection)
class WelcomeSectionAdmin(admin.ModelAdmin):
    list_display= ('chairman_name', 'welcome_message', 'chairman_image')
