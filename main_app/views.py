from main_app.pacakge import *


# Create your views here.


def index(request):
    hm=Home.objects.all()
    fac=Facilites.objects.all().order_by('id')
    welcontent=WelcomeSection.objects.all()
   
  
    dict = {'welcontent':welcontent,'hm':hm,'fac':fac}
    return render(request, 'main_app/index.html', context=dict)




def about(request):
    dict={}

    return render(request,'main_app/about.html',context=dict)



def course(request):
    dict={}

    return render(request,'main_app/courses.html',context=dict)


def course_details(request,id):
    
    dict={}

    return render(request,'main_app/course-details.html',context=dict)


def teacher(request):
    dict={}

    return render(request,'main_app/teachers.html',context=dict)


def teacher_details(request):
    dict={}
    return render(request,'main_app/teacher-details.html',context=dict)

