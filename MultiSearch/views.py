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
#     if request.method == 'GET':
#         a = Article.objects.all()
#         serializer = ArticleSerializer(a)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     if request.method == 'POST':
#         serializer = ArticleSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)

#     # if request.method == 'POST':
#     #     data = request.POST.get('search')
#     #     print(data)



            # # lesson_data = Lesson.objects.filter(lookups).distinct()
            # # tutorial_data = Tutorial.objects.filter(lookups).distinct()

            # result = chain(article_data, lesson_data, tutorial_data)
@api_view(['GET'])
def hello(request):
    print("Hii")
    return Response({'message': 'hello'})

@api_view(['GET', 'POST'])
def index(request):
    if request.method == 'POST':
        # query = request.data
        query="the-alchemist"
        if query is not None:
            # Creating lookups
            lookups = Q(title__icontains = query)
            lookups = Q(description__icontains = query)
            lookups = Q(slug__icontains = query)
            
            # Getting data from Queries
            article_data = Article.objects.filter(lookups).distinct()
            lesson_data = Lesson.objects.filter(lookups).distinct()
            tutorial_data = Tutorial.objects.filter(lookups).distinct()

            if not article_data.exists():
                article_data = Article.objects.all()
            
            if not lesson_data.exists():
                lesson_data = Lesson.objects.all()
            
            if not tutorial_data.exists():
                tutorial_data = Tutorial.objects.all()


            # Serialing the data 
            # serializer_article = ArticleSerializer(article_data, many=True)
            # serializer_lesson = LessonSerializer(lesson_data, many = True)

            # serializer_tutorial = LessonSerializer(tutorial_data, many = True)
            
            # Combining the data
            article = article_data
            tutorial = tutorial_data
            lesson = lesson_data
            data = (article,tutorial, lesson)
            
            mydata = namedtuple('Combineddata', ('article','tutorial', 'lesson'))
            Mydata = mydata(article=article, tutorial=tutorial, lesson=lesson)
            dt=TimelineSerializer(Mydata)
            print(dt.data)

            # print(article_data, lesson_data, tutorial_data, serializer_tutorial, serializer_article, serializer_lesson)
            # print(serializer_article)
            # print(article_data)
            # print(serializer_article.data)
            return Response(data= dt.data)
            
    else:
        return Response({"message": "Enter the valid query"})        

            # lookups = Q(description__icontains = query)
            # lesson_data = Lesson.objects.filter(lookups)
            # lesson_serializer = LessonSerializer(lesson_data)
            # if query == serializer_article.data['description']:
            #     return Response(serializer_article.data['description'], status=status.HTTP_202_FOUND)
            # else:
            #     return Response(serializer_article.data)

            # lookups = Q(slug__icontains = query)
            # tutorial_data = Tutorial.objects.filter(lookups)
            # tutorial_serializer = LessonSerializer(lesson_data)
            # if query == serializer_article.data['slug']:
            #     return Response(serializer_article.data['slug'], status=status.HTTP_202_FOUND)
            # else:
            #     return Response(serializer_article.data)


           
            # return Response(serializer_article.data, status = status.)
    
