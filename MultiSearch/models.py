from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank = True)
    slug = models.SlugField(blank=True, null= True)
    publish_date  = models.DateTimeField(auto_now_add=False, auto_now=False, null=True, blank=True)

    def __str__(self):
        return self.title

class Lesson(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(null=True, blank=True)
    slug     = models.SlugField(blank=True, unique=True)
    featured  = models.BooleanField(default=False)
    publish_date  = models.DateTimeField(auto_now_add=False, auto_now=False, null=True, blank=True)

    def __str__(self):
        return self.title

class Tutorial(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(null=True, blank=True)
    slug     = models.SlugField(blank=True, unique=True)
    author = models.CharField(max_length=20)
    featured  = models.BooleanField(default=False)
    publish_date  = models.DateTimeField(auto_now_add=False, auto_now=False, null=True, blank=True)

    def __str__(self):
        return self.title



