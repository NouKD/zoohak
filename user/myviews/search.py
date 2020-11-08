from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.db.models import Q

from user.models import Utilisateur


@csrf_exempt
@login_required(login_url='home')
def memo_search_user(request):
    query = request.POST.get('q')
    if query and not query.isspace():

        query = query.strip()
        utilisateur = Utilisateur.objects.filter(
            Q(first_name__icontains=query)|
            Q(last_name__icontains=query)|
            Q(email__icontains=query)|
            Q(contact__icontains=query),
            status=True
        )

        datas = {
            'success': True,
            'users': [
                {
                    'nom': u.first_name,
                    'prenom': u.last_name,
                    'email': u.email,
                    'img': u.photoprofile,
                    'id': u.id
                } for u in utilisateur.exclude(username=request.user.username).order_by('first_name')[:20]
            ]
        }

    else:
        datas = {
            'success': False
        }

    return JsonResponse(datas, safe=False)