from django.db import models



class Camera(models.Model):
    numero = models.PositiveIntegerField(default=1)
    lien_flux = models.TextField(null=True, blank=True)

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Camera'
        verbose_name_plural = 'Cameras'

    def __str__(self):
        return f'Camera {self.numero}'



class EspeceMenace(models.Model):
    STATE = [
        ('1', 'Stable'),
        ('0', 'Contraignant'),
        ('-1', 'Critique'),
    ]
    nom = models.CharField(max_length=255)
    statut = models.CharField(max_length=255, choices=STATE)
    population_estimee = models.CharField(max_length=255, null=True, blank=True, default='Inconnu')
    menace = models.CharField(max_length=255, null=True, blank=True)

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Espèce Menacée'
        verbose_name_plural = 'Espèces Menacées'

    def __str__(self):
        return f'Camera {self.nom}'



class RepartitionElephant(models.Model):
    country = models.CharField(max_length=255)
    population_estimee = models.CharField(max_length=255, null=True, blank=True, default='Inconnu')
    annee = models.DateField()

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Répartition Elephant'
        verbose_name_plural = 'Répartitions Elephants'

    def __str__(self):
        return f'Pays: {self.country} => {self.population_estimee}'
