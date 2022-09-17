from main_app.pacakge import *


# Create your views here.


def index(request):
    hm=Home.objects.all()
    fac=Facilites.objects.all().order_by('id')
    wel=Welcome.objects.all
    welcontent=ChairmanSection.objects.all()

    ev=Event.objects.all()[:4]


    dict = {'welcontent':welcontent,'hm':hm,'fac':fac,'wel':wel,'ev':ev}
    return render(request, 'main_app/index.html', context=dict)



def faclities_details(request,pk):
    fc_details=FacilitiesDetails.objects.get(title_id=pk)
    fac=Facilites.objects.get(id=pk)
    dict={'fc_details':fc_details,'fac':fac}

    return render(request,'main_app/facilities-details.html',context=dict)


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



def event(request):
    ev=Event.objects.all()

    dict={'ev':ev}

    return render(request,'main_app/event.html',context=dict)


def EventDetails(request):
    dict={}

    return render(request,'main_app/event-details.html',context=dict)



def contact(request):
    dict={}

    return render(request,'main_app/contact.html',context=dict)



def blog(request):
    dict={}

    return render(request,'main_app/blog.html',context=dict)
