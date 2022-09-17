from django.db import models
import datetime

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
    teacher_name=models.CharField(max_length=700,blank=True)
    TeacherImage=models.ImageField(upload_to='teacherprofile')
    TeacherDesignations=models.CharField(max_length=400,null=True)
    FacebookLink=models.URLField(max_length=200,blank=True,null=True)
    TwitterLink=models.URLField(max_length=200,blank=True,null=True)

    def __str__(self):
        return self.teacher_name

class TeacherDetail(models.Model):
    teacher_name=models.ForeignKey(TeacherSection,on_delete=models.CASCADE,related_name='TeacherDetail')
    teacher_information=models.TextField(max_length=8000,blank=True,null=True)



class ChairmanSection(models.Model):
    chairman_name=models.CharField(max_length=100,null=True,blank=True)
    welcome_message=models.TextField(max_length=5000,null=True,blank=True)
    chairman_image=models.ImageField(upload_to='chairman')

    def __str__(self) -> str:
        return self.chairman_name



class about(models.Model):

    about_description=models.TextField(max_length=5000,blank=True,null=True)
    about_image=models.ImageField(upload_to='chairman')

    def __str__(self) -> str:
        return str('id')


class Event(models.Model):
    event_title=models.CharField(max_length=100,blank=True,null=True)
    event_date=models.DateTimeField()
    event_time=models.CharField(max_length=40,blank=True,null=True)
    event_image=models.ImageField(upload_to='event',blank=True,null=True)

    def __str__(self) -> str:
        return self.event_title


class EventDetails(models.Model):
    event_title=models.ForeignKey(Event,on_delete=models.CASCADE,related_name='EventDetails')
    event_descriptions=models.TextField(max_length=7000,blank=True,null=True)
    event_pdf=models.FileField(upload_to='department_files')
    event_main_speaker=models.CharField(max_length=123,blank=True,null=True)

    def __str__(self) -> str:
        return str('title')



class Publications(models.Model):
    title=models.CharField(max_length=500,blank=True,null=True)
    publication_date=models.DateTimeField(blank=True,null=True)
    descriptions=models.TextField(max_length=8000,blank=True,null=True)
    image=models.ImageField(upload_to='chairman')

    def __str__(self) -> str:
        return self.title


class PublicationDetail(models.Model):
    title=models.ForeignKey(Publications,on_delete=models.CASCADE,related_name='PublicationDetail')
    author_name=models.CharField(max_length=300,blank=True,null=True)


    def __str__(self) -> str:
        return str('title')



class Research(models.Model):
    title=models.CharField(max_length=400,blank=True,null=True)
    image=models.ImageField(upload_to='chairman')
    publish_date=models.DateTimeField(blank=True,null=True)
    descriptions=models.TextField(max_length=9000,blank=True,null=True)
    def __str__(self) -> str:
        return self.title


class ResearchDetail(models.Model):
    title=models.ForeignKey(Research,on_delete=models.CASCADE,related_name='ResearchDetail')
    author_name=models.CharField(max_length=120,blank=True,null=True)

    def __str__(self)-> str:
        return str('title')
