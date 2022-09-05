from django.contrib import admin
from .models import *


# Register your models here.

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('course_title', 'course_image',
                    'course_duration','class_size','class_durations','course_descriptions')
