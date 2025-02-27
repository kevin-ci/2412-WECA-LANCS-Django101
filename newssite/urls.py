"""
URL configuration for newssite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from main import views as main_views
from articles import views as article_views

urlpatterns = [
    path('', main_views.home, name="homepage"),
    path('articles/create', article_views.create_article, name="create_article"),
    path('articles/<article_id>', article_views.view_article, name="view_article"),
    path('articles/<article_id>/edit', article_views.edit_article, name="edit_article"),
    path('articles/<article_id>/delete', article_views.delete_article, name="delete_article"),
    path('admin/', admin.site.urls),
]
