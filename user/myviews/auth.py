from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.core.validators import validate_email
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.db.models import Q

from user.models import Utilisateur



@csrf_exempt
def register_view(request):
    message, success = "Une erreur s'est produite", False
    nom = request.POST.get('nom').strip()
    prenom = request.POST.get('prenom').strip()
    email = request.POST.get('email').strip()
    password1 = request.POST.get('password1')
    password2 = request.POST.get('password2')

    if nom and prenom and email and password1 and password2:
        try:
            validate_email(email)
            assert password1 == password2
        except AssertionError:
            message, success = 'Les mots de passe ne correspondent pas', False
        except Exception:
            message, success = 'Email invalide', False
        else:
            user = Utilisateur(last_name=nom, first_name=prenom, email=email)
            user.set_password(password1)
            user.save()

            utilisateur = authenticate(username=user.username, password=password1)
            if utilisateur:
                login(request, utilisateur)
            message, success = 'Inscription effectué', True
    else:
        message, success = 'Veuillez renseigner correctement les champs', False

    datas = {
        'message': message,
        'success': success,
    }

    return JsonResponse(datas, safe=False)


@csrf_exempt
def login_view(request):
    message, success = '', False
    email = request.POST.get('email')
    password = request.POST.get('password')

    try:
        user = Utilisateur.objects.get(Q(email=email) | Q(username=email))
        utilisateur = authenticate(username=user.username, password=password)
        assert utilisateur

    except Exception as e:
        print('\n==>', e, '\n')
        message = 'Email ou mot de passe incorrect'
    
    else:
        login(request, utilisateur)
        message, success = 'Connexion effectué', True

    datas = {
        'message': message,
        'success': success,
    }

    return JsonResponse(datas, safe=False)



def logout_view(request):
    logout(request)
    return redirect('home')
