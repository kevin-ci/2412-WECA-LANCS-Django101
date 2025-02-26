from django.shortcuts import render
from .models import Article

# Create your views here.
def view_article(request, article_id):
    article = Article.objects.get(id=article_id)

    context = {
        "article": article,
    }

    return render(request, 'article.html', context)