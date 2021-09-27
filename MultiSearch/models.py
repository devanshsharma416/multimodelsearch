from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class NewUser(AbstractUser):
    class Meta:
        
        verbose_name = 'NewUser'
        verbose_name_plural = 'NewUsers'

    def __str__(self):
        return self.username

class Article(models.Model):
    title          = models.CharField(max_length=100)
    description    = models.TextField(null=True, blank = True)
    slug           = models.SlugField(blank=True, null= True)
    user           = models.ForeignKey(NewUser, on_delete=models.CASCADE, blank=True, null=True)
    summary        = models.CharField(max_length=200, null=True, blank= True)

    class Meta:
        
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'

    def __str__(self):
        return self.title

class Lesson(models.Model):
    title          = models.CharField(max_length=120)
    description    = models.TextField(null=True, blank=True)
    slug           = models.SlugField(blank=True, unique=True)
    user           = models.ForeignKey(NewUser, on_delete=models.CASCADE, blank=True, null=True)
    summary        = models.CharField(max_length=200, null=True, blank= True)
    

    class Meta:
    
        verbose_name = 'Lesson'
        verbose_name_plural = 'Lessons'


    def __str__(self):
        return self.title

class Tutorial(models.Model):
    title           = models.CharField(max_length=120)
    description     = models.TextField(null=True, blank=True)
    slug            = models.SlugField(blank=True, unique=True)
    author          = models.CharField(max_length=20)
    user            = models.ForeignKey(NewUser, on_delete=models.CASCADE, blank=True, null=True)
    

    class Meta:
        
        verbose_name = 'Tutorial'
        verbose_name_plural = 'Tutorials'


    def __str__(self):
        return self.title


class Chapter(models.Model):
    title       =     models.CharField(max_length=120)
    description =     models.TextField(null=True, blank=True)
    slug        =     models.SlugField(blank=True, unique=True)
    author      =     models.CharField(max_length=20)
    user        =     models.ForeignKey(NewUser, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        
        verbose_name = 'Chapter'
        verbose_name_plural = 'Chapters'

    def __str__(self):
        return self.title

class Book(models.Model):
    title           = models.CharField(max_length=120)
    description     = models.TextField(null=True, blank=True)
    isbn            = models.CharField(max_length=20)
    author          = models.CharField(max_length=20)
    user            = models.ForeignKey(NewUser, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        
        verbose_name = 'Book'
        verbose_name_plural = 'Books'


    def __str__(self): 
        return self.title


