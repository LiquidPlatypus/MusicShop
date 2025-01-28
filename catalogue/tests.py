import datetime

from django.test import TestCase
from django.utils import timezone

from .models import Article

class ArticleModelTests(TestCase):
	
	def test_was_published_recently_with_future_article(self):
		time = timezone.now() + datetime.timedelta(days=30)
		future_article = Article(date_ajout=time)
		self.assertIs(future_article.was_published_recently(), False)

	def test_was_published_recently_with_old_article(self):
		time = timezone.now() - datetime.timedelta(days=1, seconds=1)
		old_article = Article(date_ajout=time)
		self.assertIs(old_article.was_published_recently(), False)
		
	def test_was_published_recently_with_recent_article(self):
		time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
		recent_article = Article(date_ajout=time)
		self.assertIs(recent_article.was_published_recently(), True)