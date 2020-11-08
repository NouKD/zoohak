import codecs, random, string

from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser


def codegenerate():
    return ''.join(random.choices(string.digits+string.ascii_uppercase, k=10))


class Utilisateur(AbstractUser):
    photo = models.FileField(upload_to="images/profile", default='profile.jpg', null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    description = models.TextField(null=True, blank=True)

    facebook_link = models.URLField(null=True, blank=True, default='')
    tweeter_link = models.URLField(null=True, blank=True, default='')
    google_link = models.URLField(null=True, blank=True, default='')

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    @property
    def photoprofile(self):
        if self.photo:
            return self.photo.url
        else:
            return 'Aucune photo trouvé'

    @receiver(post_save, sender='user.Utilisateur')
    def create_username(sender, instance, created, **kwargs):
        if created and not instance.username:
            instance.username = codegenerate()
            instance.save()

    class Meta:
        verbose_name = 'Utilisateur'
        verbose_name_plural = 'Utilisateurs'
        unique_together = ['email',]
    
    def __str__(self):
        return self.get_full_name()
