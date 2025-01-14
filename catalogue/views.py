from django.shortcuts import render
from .models import Article

def articles_listing(request):
    articles = Article.objects.all()
    return render(request, 'catalogue/liste_articles.html', {'articles': articles})
