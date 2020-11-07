from django.shortcuts import render

# Create your views here.

def index(request):
    datas = {

    }
    return render(request, 'pages/index.html', datas)

def about(request):

    datas = {

    }
    return render(request, 'pages/propos.html', datas)