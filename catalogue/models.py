import datetime
from django.db import models
from django.utils import timezone
from django.conf import settings
from django.templatetags.static import static

import os

class Article(models.Model):
	nom = models.CharField(max_length=255)
	photo = models.ImageField(upload_to='photos/', blank=True, null=True)
	description = models.TextField()
	prix = models.DecimalField(max_digits=10, decimal_places=2)
	stock = models.IntegerField()
	date_ajout = models.DateTimeField(auto_now_add=True)
	
	def __str__(self):
		return self.nom
	
	def was_published_recently(self):
		now = timezone.now()
		return now - datetime.timedelta(days=1) <= self.date_ajout <= now


	@property
	def get_photo_url(self):
		if self.photo and self.photo.url.startswith('/media/'):
			return self.photo.url
		return static('catalogue/img/default.jpg')