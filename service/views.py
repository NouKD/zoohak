from django.shortcuts import render

# Create your views here.

def camera(request):
    datas = {

    }
    return render(request, 'pages/camera.html', datas)

def signup(request):
    datas = {

    }
    return render(request, 'pages/signup.html', datas)    
