import datetime
from django.db import models
from django.utils import timezone

class Article(models.Model):
    nom = models.CharField(max_length=255)
    description = models.TextField()
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    date_ajout = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nom
    
    def was_published_recently(self):
        return self.date_ajout >= timezone.now() - datetime.timedelta(days=1)
