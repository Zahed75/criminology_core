from main_app.pacakge import *


# Create your views here.


def index(request):
    dict = {}
    return render(request, 'main_app/index.html', context=dict)
