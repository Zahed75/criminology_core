from main_app.pacakge import *


# Create your views here.


def index(request):
    hm=Home.objects.all()
    fac=Facilites.objects.all().order_by('id')[:3]
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


def event(request):
    ev=Event.objects.all().order_by('id')

    dict={'ev':ev}

    return render(request,'main_app/event.html',context=dict)


def details_event(request,pk):
    ev_details=EventDetails.objects.get(event_title_id=pk)
    ev=Event.objects.get(id=pk)

    dict={'ev':ev,'ev_details':ev_details}

    return render(request,'main_app/event-details.html',context=dict)


def AboutSection(request):
    abt=about.objects.all()
    dict={'abt':abt}

    return render(request,'main_app/about.html',context=dict)



def course(request):
    dict={}

    return render(request,'main_app/courses.html',context=dict)


def course_details(request,id):

    dict={}

    return render(request,'main_app/course-details.html',context=dict)


def teacher(request):
    tc=TeacherSection.objects.all().order_by('id')

    dict={'tc':tc}

    return render(request,'main_app/teachers.html',context=dict)


def DetailsTeacher(request,pk):
    tc_details=TeacherDetail.objects.get(teacher_name_id=pk)
    tc=TeacherSection.objects.get(id=pk)
    dict={'tc_details':tc_details,'tc':tc}
    return render(request,'main_app/teacher-details.html',context=dict)




def contact(request):
    dict={}

    return render(request,'main_app/contact.html',context=dict)



def research(request):
    rc=Research.objects.all().order_by('id')

    dict={'rc':rc}

    return render(request,'main_app/research.html',context=dict)

def research_details(request,pk):
    rc_details=ResearchDetail.objects.get(title_id=pk)
    rc=Research.objects.get(id=pk)

    dict={'rc_details':rc_details,'rc':rc}

    return render(request,'main_app/research-details.html',context=dict)


def pub(request):
    pb=Publications.objects.all().order_by('id')

    dict={'pb':pb}

    return render(request,'main_app/publications.html',context=dict)


def pub_details(request,pk):
    ev=Event.objects.all()[:3]
    pb_details=PublicationDetail.objects.get(title_id=pk)
    pb=Publications.objects.get(id=pk)
    dict={'pb_details':pb_details,'pb':pb,'ev':ev}


    return render(request,'main_app/publication-details.html',context=dict)
