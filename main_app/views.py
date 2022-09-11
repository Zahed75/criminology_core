from main_app.pacakge import *


# Create your views here.


def index(request):
    welcontent=WelcomeSection.objects.all()
    course_info=Course.objects.all()
   
    dict = {'welcontent':welcontent,'course_info':course_info}
    return render(request, 'main_app/index.html', context=dict)




def about(request):
    dict={}

    return render(request,'main_app/about.html',context=dict)



def course(request):
    dict={}

    return render(request,'main_app/course.html',context=dict)



def teacher(request):
    dict={}

    return render(request,'main_app/teachers.html',context=dict)


def teacher_details(request):
    dict={}
    return render(request,'main_app/teacher_details.html',context=dict)