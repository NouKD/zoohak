from django.shortcuts import render
from .models import About
from service.models import EspeceMenace, RepartitionElephant
from django.contrib.auth.decorators import login_required



# Create your views here.
@login_required(login_url='signup')
def index(request):
    especes = EspeceMenace.objects.filter(status=True)
    elephants = RepartitionElephant.objects.filter(status=True)

    datas = {
        'especes': especes,
        'elephants': elephants,
    }

    return render(request, 'pages/index.html', datas)



def about(request):
    about = About.objects.filter(status=True).first()
    return render(request, 'pages/propos.html', locals())