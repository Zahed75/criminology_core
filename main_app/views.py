from main_app.pacakge import *


# Create your views here.


def index(request):
    welcontent=WelcomeSection.objects.all()
    course_info=Course.objects.all()
   
    dict = {'welcontent':welcontent,'course_info':course_info}
    return render(request, 'main_app/index.html', context=dict)
