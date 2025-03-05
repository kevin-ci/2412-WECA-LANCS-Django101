from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Article
from .forms import ArticleForm
from django.contrib.auth.decorators import login_required
from utils import superuser_required

# Create your views here.
def view_article(request, article_id):
    article = Article.objects.get(id=article_id)

    context = {
        "article": article,
    }

    return render(request, 'article.html', context)

@login_required
def create_article(request):
    if request.method == 'POST':
        article_form = ArticleForm(request.POST)
        if article_form.is_valid():
            article_form.save()
            messages.success(request, "Article created!")
            return redirect("homepage")
        else:
            messages.error(request, "Form invalid!")
            return redirect("homepage")
    else:
        article_form = ArticleForm()
        context = {
            "form": article_form,
        }
        return render(request, 'create_article.html', context)
    
@superuser_required
def edit_article(request, article_id):
    article = Article.objects.get(id=article_id)

    if request.method == 'POST':
        article_form = ArticleForm(request.POST, instance=article)
        if article_form.is_valid():
            article_form.save()
            messages.success(request, "Article updated!")
            return redirect("homepage")
        else:
            messages.error(request, "Form invalid!")
            return redirect("homepage")
    else:
        article_form = ArticleForm(instance=article)
        context = {
            "form": article_form,
        }
        return render(request, 'create_article.html', context)
    
@superuser_required
def delete_article(request, article_id):
    if request.method == 'POST':
        article = Article.objects.get(id=article_id)
        article.delete()
        messages.success(request, "Article deleted!")
        return redirect("homepage")
    else:
        return render(request, 'delete_article.html')