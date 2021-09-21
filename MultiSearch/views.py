from django.db.models.query_utils import FilteredRelation
from MultiSearch.serializers import (ArticleSerializer, 
        LessonSerializer, 
        TutorialSerializer, 
        ChapterSerializer, 
        BookSerializer)
from django.db import models
from django.shortcuts import render
from django.db.models import Q
from .models import Article, Chapter, Lesson, Tutorial, Book
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .filters import ArticleFilter, LessonFilter, TutorialFilter
from itertools import chain


# class ArticleDocumentView(DocumentViewSet):
#     document = ArticleDocument
#     serializer_class = ArticleDocumentSerializer

#     # filter_backends = [
#     #     FilteringFilterBackend, 
#     #     CompoundSearchFilterBackend
#     # ]        

#     search_fields = ('title', 'description')
#     multi_match_search_fields = ('title', 'description')
#     filter_fields = {
#         'title' : 'title',
#         'description' : 'description'
# #     }
class IndexView(APIView):
    

    """Create get method to perform get request""" 
    
    def get(self, request, format = None):
        
        query = request.GET.get('query')
       
        article_final_data = []
        lesson_final_data = []
        tutorial_final_data = []
        chapter_final_data = []
        book_final_data = []

        article_data = Article.objects.all()
        lesson_data = Lesson.objects.all()
        tutorial_data = Tutorial.objects.all()
        chapter_data = Chapter.objects.all()
        book_data = Book.objects.all()


        if query is not None:
            
            """Creating Queryset for desired data"""
            article_data1 = article_data.filter(title__icontains = query)
            article_data2 = article_data.filter(description__icontains = query).exclude(title__icontains = query)
            article_final_data  = list(chain(article_data1, article_data2))
            print(article_final_data)
             
            lesson_data1 = lesson_data.filter(description__icontains = query)
            lesson_data2 = lesson_data.filter(slug__icontains = query).exclude(description__icontains =query)
            lesson_final_data = list(chain(lesson_data1, lesson_data2))

            tutorial_data1 = tutorial_data.filter(slug__icontains = query)
            tutorial_data2 = tutorial_data.filter(title__icontains = query).exclude(slug__icontains =query)
            tutorial_final_data = list(chain(tutorial_data1, tutorial_data2))

            chapter_data1 = chapter_data.filter(description__icontains = query)
            chapter_data2 = chapter_data.filter(author__icontains = query).exclude(description__icontains =query)
            chapter_final_data = list(chain(chapter_data1, chapter_data2))

            book_data1 = book_data.filter(title__icontains = query)
            book_data2 = book_data.filter(author__icontains = query).exclude(title__icontains =query)
            book_final_data = list(chain(book_data1, book_data2))


        """Serializing the Queryset"""
        serializer_article = ArticleSerializer(article_final_data, many=True)
        serializer_lesson = LessonSerializer(lesson_final_data, many = True)
        serializer_tutorial = TutorialSerializer(tutorial_final_data, many=True)
        serializer_chapter = ChapterSerializer(chapter_final_data, many = True)
        serializer_book = BookSerializer(book_final_data, many = True)   
        
        return Response({"Article":serializer_article.data,
                                "Lesson" :serializer_lesson.data,
                                "Tutorial": serializer_tutorial.data,
                                "Chapter": serializer_chapter.data,
                                "Book": serializer_book.data}, status=200)
                



# class IndexView(APIView):
    
#     def get(self, request, format = None):
        
        
#         query = request.GET.get('query', None)
        
#         if query is not None:

#             queryset1 = Article.objects.filter(Q(title__icontains = query) | (Q(description__icontains = query)))
#             queryset2 = Lesson.objects.filter(Q(title__icontains = query) | (Q(description__icontains = query)))
#             queryset3 = Tutorial.objects.filter(Q(title__icontains = query) | (Q(description__icontains = query)))

#             filterset1 = ArticleFilter(request.GET, queryset = queryset1)
#             filterset2 = LessonFilter(request.GET, queryset = queryset2)
#             filterset3 = LessonFilter(request.GET, queryset = queryset3)
        
#             # Making Queryset as a 
#             new_queryset1 = filterset1.qs
#             new_queryset2 = filterset2.qs
#             new_queryset3 = filterset3.qs
            
#         serializer_article = ArticleSerializer(new_queryset1, many=True)
#         serializer_lesson = LessonSerializer(new_queryset2, many=True)
#         serializer_tutorial = TutorialSerializer(new_queryset3, many = True)
        
#         return Response({'Article': serializer_article.data, 'Lesson': serializer_lesson.data, 'Tutorial': serializer_tutorial.data})

        
       

# # #         if filterset.is_valid():
# # #             queryset = filterset.qs
# # #             serializer_lesson = LessonSerializer(queryset, many=True)
# # #             return Response(serializer_lesson.data)
















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
        