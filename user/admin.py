from django.contrib import admin
from django.utils.safestring import mark_safe
from django.contrib.auth.admin import UserAdmin

from . import models


@admin.register(models.Utilisateur)
class UtilisateurAdmin(UserAdmin):
    list_display = ('username', 'last_name', 'first_name', 'email', 'img',)
    list_display_links = ('username', 'last_name', 'first_name', 'email', 'img')


    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('photo', 'facebook_link', 'tweeter_link', 'google_link', 'description')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('photo', 'facebook_link', 'tweeter_link', 'google_link', 'description')}),
    )

    actions = ["activate", "deactivate"]

    def deactivate(self, request, queryset):
        queryset.update(status=False)
        self.message_user(request, "Désactivation(s) effectué(s)")
    deactivate.short_description = "Désactiver les utilisateurs selectionnés"

    def activate(self, request, queryset):
        queryset.update(status=True)
        self.message_user(request, "Activation(s) effectué(s)")
    activate.short_description = "Activer les utilisateurs selectionnés"


    def img(self, obj):
        return mark_safe(f'<img src="{obj.photoprofile}" style="height:60px; width:60px">')
    img.short_description = 'Photo de profile'

    def log_addition(self, *args):
        return

    def log_change(self, *args):
        return

    def log_deletion(self, *args):
        return


styles = 'color: #79aec8;font-weight: bold;font-size: 2em;font-variant: small-caps;letter-spacing: 5px;text-transform: capitalize;-webkit-text-emphasis-position: under;-webkit-text-emphasis-style: open;'
admin.site.site_header = mark_safe(f'<h1 style="{styles}">RyLip</h1>')
admin.site.index_title = "Bienvenu dans l'administration"
admin.site.site_title = 'Admin'
