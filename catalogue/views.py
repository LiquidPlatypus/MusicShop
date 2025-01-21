from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Article

class ListingView(generic.ListView):
	template_name = 'catalogue/listing.html'
	context_object_name = 'latest_articles_list'
	
	def get_queryset(self):
		return Article.objects.order_by('-date_ajout')[:5]

class DetailsView(generic.DetailView):
	model = Article
	template_name = 'catalogue/details.html'

def article_page(request, article_id):
	article = get_object_or_404(Article, pk=article_id)