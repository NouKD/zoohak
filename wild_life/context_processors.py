from website.models import WebSite


def datas(request):
    website = WebSite.objects.filter(status=True).first()
    return locals()