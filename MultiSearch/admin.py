from django.contrib import admin
from .models import Article, Lesson, Tutorial

@admin.register(Article)
class AuthorAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title', ), }

@admin.register(Lesson)
class AuthorAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title', ), }

@admin.register(Tutorial)
class AuthorAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title', ), }

# Register your models here.
