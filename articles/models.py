from django.db import models

# Create your models here.
class Article(models.Model):
    headline = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    image = models.URLField()
    copy = models.TextField()

    def __str__(self):
        return f"{self.headline} by {self.author}"