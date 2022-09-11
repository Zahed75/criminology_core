from main_app.pacakge import *


# Create your views here.


def index(request):
    welcontent=WelcomeSection.objects.all()
   
    dict = {'welcontent':welcontent}
    return render(request, 'main_app/index.html', context=dict)
