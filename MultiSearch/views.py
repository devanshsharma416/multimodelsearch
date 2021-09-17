# from django.db.models import query
from django.http.response import JsonResponse
from MultiSearch.serializers import ArticleSerializer, LessonSerializer, TutorialSerializer
from django.shortcuts import render
from django.db.models import Q
from .models import Article, Lesson, Tutorial
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from collections import namedtuple


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

# @api_view(['GET'])
# def index(request):
 
#     query = request.GET.get('query', None)
#     print(query)
#     if query is not None:
#         # Getting data from Queries

#             article_data = (Article.objects.filter(Q(title__icontains = query) | Q (description__icontains = query)).distinct()).order_by("title")
#             # article_data = (Article.objects.filter(title__icontains = query) | Article.objects.filter(description__icontains = query)).distinct()
#             print(article_data)
            
#             lesson_data = (Lesson.objects.filter(Q(description__icontains = query) | Q(slug__icontains = query)).distinct()).order_by("slug")
#             # lesson_data = (Lesson.objects.filter(description__icontains = query) | Lesson.objects.filter(slug__icontains = query)).distinct()
#             print(lesson_data)
            
#             tutorial_data = (Tutorial.objects.filter(Q(slug__icontains = query) | Q(title__icontains = query)).distinct()).order_by("title")
#             # tutorial_data = (Tutorial.objects.filter(slug__icontains = query) | Tutorial.objects.filter(title__icontains = query)).distinct()
#             print(tutorial_data)
            
#             serializer_article = ArticleSerializer(article_data, many=True)
#             serializer_lesson = LessonSerializer(lesson_data, many = True)
#             serializer_tutorial = TutorialSerializer(tutorial_data, many=True)
            
#             print(serializer_tutorial.data)

#             if not article_data.exists() and not(lesson_data.exists()) and not(tutorial_data):
#                 message = {"message": "Enter the valid value"}
#                 return Response(message)
        
#             # else:
#             #     print("Hello")
#             #     if article_data.exists(): 
#             #         print("hello") 
#             #         return Response(serializer_article.data)
#             #     elif lesson_data.exists():  
#             #         print("hii")
#             #         return Response(serializer_lesson.data)
#             #     else: 
#             #         return Response(serializer_tutorial.data)

#             if len(article_data) != 0:
#                 return Response(serializer_article.data)
#             elif len(lesson_data) != 0:
#                 return Response(serializer_lesson.data)    
#             elif len(tutorial_data) !=0 :
#                 return Response(serializer_tutorial.data)

#             return Response({"message": "badiya"})
                
            
    
#     else:
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
#             'article':article, 'lesson': lesson,  'tutorial': tutorial
#         })
            
class IndexView(APIView):

    """Create get method to perform get request""" 

    def get(self, request, format = None):
        query = request.GET.get('query')

        article_data = Article.objects.all()
        lesson_data = Lesson.objects.all()
        tutorial_data = Tutorial.objects.all()

        if query is not None:
            
            """Creating Queryset for desired data"""
            article_data = article_data.filter(Q(title__icontains = query) | Q (description__icontains = query)).distinct()
            lesson_data = lesson_data.filter(Q(description__icontains = query) | Q(slug__icontains = query)).distinct()
            tutorial_data = tutorial_data.filter(Q(slug__icontains = query) | Q(title__icontains = query)).distinct()
            
        """Serializing the Queryset"""
        serializer_article = ArticleSerializer(article_data, many=True)
        serializer_lesson = LessonSerializer(lesson_data, many = True)
        serializer_tutorial = TutorialSerializer(tutorial_data, many=True)

        """Check if data is not existed"""
        # if not article_data.exists() and not(lesson_data.exists()) and not(tutorial_data.exists()):
            
        return Response({"article":serializer_article.data, 
                            "lesson" :serializer_lesson.data,
                            "tutorial": serializer_tutorial.data}, status=200)
                



















# Getting data from Queries
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
        