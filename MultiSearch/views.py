# from django.db.models import query
from django.http.response import JsonResponse
from MultiSearch.serializers import ArticleSerializer, LessonSerializer, TutorialSerializer, TimelineSerializer
from django.shortcuts import render
from django.db.models import Q, query
from .models import Article, Lesson, Tutorial
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from collections import namedtuple

# # Create your views here.
# # @api_view(['GET', 'POST'])
# def index(request):
#     if request.method == 'POST':
#         query = request.POST.get('search')
#         if query is not None:
#             lookups = Q(title__icontains = query) | Q(description__icontains=query) | Q(slug__icontains=query)

#             article_data = Article.objects.filter(lookups).distinct()
#             lesson_data = Lesson.objects.filter(lookups).distinct()
#             tutorial_data = Tutorial.objects.filter(lookups).distinct()

#             result = chain(article_data, lesson_data, tutorial_data)

#         else:
#             return Tutorial.objects.all()
            
#     else:
#         return render(request, 'search.html')
            
#     context = {
#             'result': result,
#             'query':query
            
#             }   
#     return render(request, 'search.html', context)


# @api_view(['GET', 'POST'])
# def index(request):
#     if request.method == 'POST':
#         # query = request.data
#         query=""
#         if query is not None:
#             # Getting data from Queries
#             article_data = Article.objects.filter(Q(title__icontains = query)).distinct()
#             lesson_data = Lesson.objects.filter(Q(description__icontains = query)).distinct()
#             tutorial_data = Tutorial.objects.filter(Q(slug__icontains = query)).distinct()

#             if not article_data.exists() and not(lesson_data.exists()) and not(tutorial_data):
#                 message = {"message": "Enter the valid value"}
#                 return Response(message)
            
            
#         article_data = Article.objects.all()
#         lesson_data = Lesson.objects.all()
#         tutorial_data = Tutorial.objects.all()
        
#         serializer_article = ArticleSerializer(article_data, many=True)
#         serializer_lesson = LessonSerializer(lesson_data, many = True)
#         serializer_tutorial = TutorialSerializer(article_data, many=True)
        
#         article = serializer_article.data
#         tutorial = serializer_tutorial.data
#         lesson = serializer_lesson.data
        
#         return Response({
#             'article':article,
#             'lesson': lesson, 
#             'tutorial': tutorial
#         })

        
            
    
            
            
#             # if not lesson_data.exists():
#             #     lesson_data = Lesson.objects.all()
            
#             # if not tutorial_data.exists():
#             #     tutorial_data = Tutorial.objects.all()


#             # # Serialing the data 
#             # serializer_article = ArticleSerializer(article_data, many=True)
#             # serializer_lesson = LessonSerializer(lesson_data, many = True)
#             # serializer_tutorial = LessonSerializer(tutorial_data, many = True)
            
#             # Merging the queries the data
#             # article_value = article_data
#             # tutorial_value = tutorial_data
#             # lesson_value = lesson_data
#             # # data = (article_value,tutorial_value, lesson_value)
            
#             # # Combining all the data
#             # combined_data = namedtuple('Combineddata', ('article','tutorial', 'lesson'))
#             # Mydata = combined_data(article=article_value, tutorial=tutorial_value, lesson=lesson_value)
#             # serializer_dt=TimelineSerializer(Mydata)
#             # print(serializer_dt.data)

           
#             # return Response(data = serializer_dt.data)
            
#     else:
#         return Response({"message": "Enter the valid query"})        

            
 # print(article_data, lesson_data, tutorial_data, serializer_tutorial, serializer_article, serializer_lesson)
            # print(serializer_article)
            # print(article_data)
            # print(serializer_article.data)

@api_view(['GET'])
def index(request):
 
    query=request.GET.get('query', None)
    if query is not None:
        # Getting data from Queries
            article_data = Article.objects.filter(Q(title__icontains = query)).distinct()
            lesson_data = Lesson.objects.filter(Q(description__icontains = query)).distinct()
            tutorial_data = Tutorial.objects.filter(Q(slug__icontains = query)).distinct()

            if not article_data.exists() and not(lesson_data.exists()) and not(tutorial_data):
                message = {"message": "Enter the valid value"}
                return Response(message)

            (Article.objects.filter(title__icontains = query) | Article.objects.filter(description__icontains = query)).distinct()
    
    
    
    else:
        article_data = Article.objects.all()
        lesson_data = Lesson.objects.all()
        tutorial_data = Tutorial.objects.all()
        
        serializer_article = ArticleSerializer(article_data, many=True)
        serializer_lesson = LessonSerializer(lesson_data, many = True)
        serializer_tutorial = TutorialSerializer(article_data, many=True)
        
        article = serializer_article.data
        tutorial = serializer_tutorial.data
        lesson = serializer_lesson.data
        
        return Response({
            'article':article, 'lesson': lesson,  'tutorial': tutorial
        })
            
            




















# 
# 
# 
# 
# 
# 
# # Getting data from Queries
#         article_data = Article.objects.filter(Q(title__icontains = query) & Q(description__icontains = query)).distinct()
#         lesson_data = Lesson.objects.filter(Q(description__icontains = query) & Q(slug__icontains = query)).distinct()
#         tutorial_data = Tutorial.objects.filter(Q(slug__icontains = query) & Q(title__icontains = query)).distinct()

#         if not article_data.exists():
#             article_data = Article.objects.all()
            
#         if not lesson_data.exists():
#             lesson_data = Lesson.objects.all()
            
#         if not tutorial_data.exists():
#             tutorial_data = Tutorial.objects.all()  

#             # Serialing the data 
#         serializer_article = ArticleSerializer(article_data, many=True)
#         serializer_lesson = LessonSerializer(lesson_data, many = True)
#         serializer_tutorial = LessonSerializer(tutorial_data, many = True)
        
   

#             # # Merging the queries the data
#             # article_value = article_data
#             # tutorial_value = tutorial_data
#             # lesson_value = lesson_data
#             # # data = (article_value,tutorial_value, lesson_value)
            
#             # Combining all the data
#             combined_data = namedtuple('Combineddata', ('article','tutorial', 'lesson'))
#             Mydata = combined_data(article=article_value, tutorial=tutorial_value, lesson=lesson_value)
#             serializer_dt=TimelineSerializer(Mydata)
#             print(serializer_dt.data)

           
#             return Response(data = serializer_dt.data)
            
#     else:
        