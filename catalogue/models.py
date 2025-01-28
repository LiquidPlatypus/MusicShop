import datetime
from django.db import models
from django.utils import timezone

class Article(models.Model):
	nom = models.CharField(max_length=255)
	photo = models.ImageField(upload_to='photos/%Y/%m/%d/', default="catalogue/img/default.jpg")
	description = models.TextField()
	prix = models.DecimalField(max_digits=10, decimal_places=2)
	stock = models.IntegerField()
	date_ajout = models.DateTimeField(auto_now_add=True)
	
	def __str__(self):
		return self.nom
	
	def was_published_recently(self):
		now = timezone.now()
		return now - datetime.timedelta(days=1) <= self.date_ajout <= now
