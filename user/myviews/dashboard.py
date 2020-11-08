from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.views.decorators.csrf import csrf_exempt
from django.core.validators import validate_email
from django.shortcuts import render, redirect
from django.http import JsonResponse
import re



def validate_contact(tel):
    regex = "^((\+)?[ ]?(225)+)?[ ]?[\d]{1,}([/ _-]?[\d]{2,})+$"
    reg = re.match(regex, tel)
    if not reg:
        return False
    else:
        return True


def validate_email2(email):
    try:
        validate_email(email)
    except Exception:
        return False
    else:
        return True




@login_required(login_url='home')
def dashboard_view(request):

    datas = {
        'this_page': 'Profil Update',
    }

    return render(request, "pages/user/dashboard.html", datas)



@csrf_exempt
@login_required(login_url='home')
def post_info_pressonnelle(request):
    message, success = '', False
    file = request.FILES.get("file")
    nom = request.POST.get('nom')
    prenom = request.POST.get('prenom')
    clear_photo = request.POST.get('clear_photo')

    if not nom or not prenom or nom.isspace() or prenom.isspace():
        message, success = 'Veuillez renseigner correctement les champs', False
        # message = "Type de Fichier Non, prise en charge"
    else:
        request.user.last_name = nom
        request.user.first_name = prenom
        if file and not clear_photo == 'true':
            request.user.photo = file
        if clear_photo == 'true':
            request.user.photo = None
        request.user.save()
        message, success = 'Modification effectué', True

    datas = {
        'message': message,
        'success': success,
        'src': request.user.photoprofile,
    }

    return JsonResponse(datas, safe=False)



@csrf_exempt
@login_required(login_url='home')
def post_info_supplementaire(request):

    message, success = '', False
    email = str(request.POST.get('email')).strip()
    contact = str(request.POST.get('contact')).strip()
    sexe = str(request.POST.get('sexe')).strip()
    motcle = str(request.POST.get('motcle')).strip()

    if not email or not sexe:
        message, success = 'Veuillez renseigner correctement les champs', False
    elif sexe.lower() not in ['homme', 'femme', 'autres']:
        message, success = 'Veuillez selectionner un genre valide', False
    elif contact and not validate_contact(contact):
        message, success = 'Contact invalide', False
    elif not validate_email2(email):
        message, success = 'Email invalide', False
    else:
        request.user.sexe = sexe.title()
        request.user.email = email
        request.user.contact = contact
        request.user.mots_cle = motcle
        request.user.save()
        message, success = 'Modification effectué', True

    datas = {
        'message': message,
        'success': success,
        'src': request.user.photoprofile,
    }

    return JsonResponse(datas, safe=False)



@csrf_exempt
@login_required(login_url='home')
def post_mot_de_passe(request):
    message, success = '', False
    password = str(request.POST.get('password'))
    password1 = str(request.POST.get('password1'))
    password2 = str(request.POST.get('password2'))

    if not password1.strip() or not password2.strip():
        message, success = 'Veuillez renseigner correctement les champs', False
    elif password1 != password2:
        message, success = 'Les mots de passe ne correspondent pas', False
    elif not request.user.check_password(password):
        message, success = 'Mot de passe précédent incorrect', False
    else:
        request.user.set_password(password1)
        request.user.save()
        login(request, request.user)
        message, success = 'Modification effectué', True

    datas = {
        'message': message,
        'success': success,
    }

    return JsonResponse(datas, safe=False)

