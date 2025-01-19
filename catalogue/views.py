from django.shortcuts import render, get_object_or_404
from .models import Article

def listing(request):
	latest_articles_list = Article.objects.order_by('-date_ajout')[:5]
	context = {'latest_articles_list': latest_articles_list}
	return render(request, 'catalogue/listing.html', context)

def details(request, article_id):
	article = get_object_or_404(Article, pk=article_id)
	return render(request, 'catalogue/details.html', {'article': article})
