from django.contrib import admin
from django.utils.safestring import mark_safe
from actions.action import Action
from . import models


@admin.register(models.WebSite)
class WebSiteAdmin(Action):
    list_display = ('img', 'nom', 'date_update', 'date_add', 'status',)
    list_display_links = ('nom', 'img', 'date_update', 'date_add')
    style = "height:60px; width:60px; border-radius:5px; border:2px solid #0af;"

    def img(self, obj):
        try:
            return mark_safe(f'<img src="{obj.logo.url}" style="{self.style}">')
        except (FileNotFoundError, ValueError) as e:
            return 'Aucun Fichier'
    img.short_description = 'Logo'


@admin.register(models.About)
class AboutAdmin(Action):
    list_display = ('__str__', 'date_add', 'date_update', 'status',)
    list_display_links = ('__str__', 'date_add', 'date_update',)


