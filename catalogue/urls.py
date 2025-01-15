from django.urls import path
from .views import articles_listing

urlpatterns = [
	path('', articles_listing, name='liste_articles'),
]