from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='signup')
def camera(request):
    datas = {

    }
    return render(request, 'pages/camera.html', datas)


def signup(request):
    datas = {

    }
    return render(request, 'pages/signup.html', datas)    
