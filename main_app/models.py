from django.db import models


# Create your models here.


class Course(models.Model):
    course_title = models.CharField(max_length=500)
    course_image = models.ImageField(upload_to='course_images')
    course_duration=models.CharField(max_length=20,blank=True,null=True)
    class_size=models.CharField(max_length=20)
    class_durations=models.CharField(max_length=20)
    course_descriptions = models.TextField(max_length=1000, blank=True, null=True)

    def __str__(self):
        return self.course_title


class CourseDetails(models.Model):
    course_title=models.ForeignKey(Course,on_delete=models.CASCADE,related_name='courseDetails')
    course_instructor=models.CharField(max_length=200,blank=True,null=True)
    instructor_fb=models.URLField(max_length=20,blank=True,null=True)
    instructor_twitter=models.URLField(max_length=20,blank=True,null=True)

    def __str__(self):
        return str(self.course_title)