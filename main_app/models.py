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


class CourseDetail(models.Model):
    course_title=models.ForeignKey(Course,on_delete=models.CASCADE,related_name='courseDetails')
    course_instructor=models.CharField(max_length=200,blank=True,null=True)
    instructor_designation=models.CharField(max_length=900)
    instructor_fb=models.URLField(max_length=200,blank=True,null=True)
    instructor_twitter=models.URLField(max_length=200,blank=True,null=True)

    def __str__(self):
        return str(self.course_title)




class TeacherSection(models.Model):
    TeacherName=models.CharField(max_length=700,blank=True)
    TeacherImage=models.ImageField(upload_to='teacherprofile')
    TeacherDesignations=models.CharField(max_length=400,null=True)


    def __str__(self):
        return self.TeacherName

class TeacherDetail(models.Model):
    TeacherName=models.ForeignKey(TeacherSection,on_delete=models.CASCADE,related_name='TeacherDetail')
