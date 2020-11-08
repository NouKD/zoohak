from django.contrib import admin
from django.utils.safestring import mark_safe
from actions.action import Action
from . import models


@admin.register(models.Camera)
class CameraAdmin(Action):
    list_display = ('numero', 'date_update', 'date_add', 'status',)
    list_display_links = ('numero', 'date_update', 'date_add')



@admin.register(models.EspeceMenace)
class EspeceMenaceAdmin(Action):
    list_display = ('nom', 'statut', 'population_estimee', 'menace', 'date_update', 'date_add', 'status')
    list_display_links = ('nom', 'statut', 'population_estimee', 'menace', 'date_update', 'date_add')



@admin.register(models.RepartitionElephant)
class RepartitionElephantAdmin(Action):
    list_display = ('country', 'population_estimee', 'annee', 'date_update', 'date_add', 'status')
    list_display_links = ('country', 'population_estimee', 'annee', 'date_update', 'date_add')


