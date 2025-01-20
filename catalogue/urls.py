from django.urls import path

from . import views

app_name = "catalogue"
urlpatterns = [
	path('', views.listing, name='listing'),
	path('<int:article_id>/', views.details, name='details'),
	path('<int:article_id>/article_page/', views.article_page, name='article_page'),
]