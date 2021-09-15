from django.db.models import query
from django.shortcuts import render
from django.db.models import Q
from .models import Article, Lesson, Tutorial
from itertools import chain

# Create your views here.

def index(request):
    if request.method == 'POST':
        query = request.POST.get('search')
        if query is not None:
            lookups = Q(title__icontains = query) | Q(description__icontains=query) | Q(slug__icontains=query)

            article_data = Article.objects.filter(lookups).distinct()
            lesson_data = Lesson.objects.filter(lookups).distinct()
            tutorial_data = Tutorial.objects.filter(lookups).distinct()

            result = chain(article_data, lesson_data, tutorial_data)
    else:
        return render(request, 'search.html')
            
    context = {
            'result': result,
            'query':query
            
            }   
    return render(request, 'search.html', context)