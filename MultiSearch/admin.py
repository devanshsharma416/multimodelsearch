from django.contrib import admin
from .models import (NewUser,
                    Article, 
                    Lesson, 
                    Tutorial,
                    Chapter,
                    Book)

@admin.register(NewUser)
class AuthorAdmin(admin.ModelAdmin):
   pass

@admin.register(Article)
class AuthorAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title', ), }

@admin.register(Lesson)
class AuthorAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title', ), }

@admin.register(Tutorial)
class AuthorAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title', ), }

@admin.register(Chapter)
class AuthorAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title', ), }

@admin.register(Book)
class AuthorAdmin(admin.ModelAdmin):
   pass

