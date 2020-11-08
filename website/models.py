from django.db import models



class WebSite(models.Model):
    nom = models.CharField(max_length=255, default='Wild Life', null=True, blank=True)
    logo = models.FileField(upload_to='images/website', null=True, blank=True)
    favicon = models.FileField(upload_to='images/website', null=True, blank=True)
    copyright = models.CharField(max_length=255, default='', null=True, blank=True)

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'WebSite'
        verbose_name_plural = 'WebSites'

    def __str__(self):
        return self.nom



class About(models.Model):
    description = models.TextField()
    en_savoir_plus = models.TextField()
    
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'About'
        verbose_name_plural = 'Abouts'

    def __str__(self):
        return f'{ self.id } : { self.date_add }'


