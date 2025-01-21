from django.urls import path

from . import views

app_name = "catalogue"
urlpatterns = [
	path('', views.ListingView.as_view(), name='listing'),
	path('<int:pk>/', views.DetailsView.as_view(), name='details'),
	path('<int:article_id>/article_page/', views.article_page, name='article_page'),
]