from django.db import models


# Create your models here.


class Home(models.Model):
    heading=models.CharField(max_length=500,blank=True,null=True)
    sub_heading=models.CharField(max_length=400,null=True,blank=True)
    
    def __str__(self) -> str:
        return self.heading

class Welcome(models.Model):
    descriptions=models.TextField(max_length=1000,null=True,blank=True)

    def __str__(self) -> str:
        return self.descriptions


class Facilites(models.Model):
    title=models.CharField(max_length=400,blank=True,null=True)
    image=models.ImageField(upload_to='facilites')
    heading=models.CharField(max_length=5000,blank=True,null=True)
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title


class FacilitiesDetails(models.Model):
    title=models.ForeignKey(Facilites,on_delete=models.CASCADE,related_name='FacilitiesDetails')
    descriptions=models.TextField(max_length=7000,blank=True,null=True)
    teacher_name=models.CharField(max_length=500,blank=True,null=True)
    teacher_designation=models.CharField(max_length=500,null=True,blank=True)
    fb_link=models.URLField(max_length=500,null=True,blank=True)
    twitter_link=models.URLField(max_length=500,null=True,blank=True)

    def __str__(self) -> str:
        return str('title')

class TeacherSection(models.Model):
    TeacherName=models.CharField(max_length=700,blank=True)
    TeacherImage=models.ImageField(upload_to='teacherprofile')
    TeacherDesignations=models.CharField(max_length=400,null=True)


    def __str__(self):
        return self.TeacherName

class TeacherDetail(models.Model):
    TeacherName=models.ForeignKey(TeacherSection,on_delete=models.CASCADE,related_name='TeacherDetail')
    FacebookLink=models.URLField(max_length=200,blank=True,null=True)
    TwitterLink=models.URLField(max_length=200,blank=True,null=True)


class ChairmanSection(models.Model):
    chairman_name=models.CharField(max_length=100,null=True,blank=True)
    welcome_message=models.TextField(max_length=5000,null=True,blank=True)
    chairman_image=models.ImageField(upload_to='chairman')

    def __str__(self) -> str:
        return self.chairman_name

