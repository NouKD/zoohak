from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from django.core.validators import validate_email
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import JsonResponse

from user.models import Utilisateur



@csrf_exempt
def login_view(request):
    message, success, url = 'Email ou mot de passe incorrect', False, ''
    email = request.POST.get('email')
    password = request.POST.get('password')
    user = Utilisateur.objects.filter(email=email).first()

    if user:
        utilisateur = authenticate(username=user.username, password=password)
        if utilisateur:
            login(request, utilisateur)
            message, success = 'Connexion effectué', True
            url = reverse('index', kwargs={})

    datas = {
        'message': message,
        'success': success,
        'url': url,
    }

    return JsonResponse(datas, safe=False)



def logout_view(request):
    logout(request)
    return redirect('index')