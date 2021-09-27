from django.db.models import query
from MultiSearch.serializers import (ArticleSerializer, 
        LessonSerializer, NewUserSerializer, 
        TutorialSerializer, 
        ChapterSerializer, 
        BookSerializer)
from .models import Article, Chapter, Lesson, Tutorial, Book, NewUser
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from itertools import chain
from django.db.models import Q
from drf_multiple_model.views import ObjectMultipleModelAPIView
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

'''Creating class based API VIew'''
class IndexView(APIView):
    """Create get method to perform get request""" 
    @method_decorator(cache_page(60*60*2))
    def get(self, request, format = None):
        
        # Getting query request
        query = request.GET.get('query')
       
        # declaring variable to remove the unbound error
        article_final_data     =    []
        lesson_final_data      =    []
        tutorial_final_data    =    []
        chapter_final_data     =    []
        book_final_data        =    []

        # Getting all the data from the Models
        article_data          = Article.objects.all()
        lesson_data           = Lesson.objects.all()
        tutorial_data         = Tutorial.objects.all()
        chapter_data          = Chapter.objects.all()
        book_data             = Book.objects.all()


        if query is not None:
            
            """Creating Queryset for desired data"""
            article_data1 = article_data.filter(title__icontains = query)
            # We have used the exlude the duplicacy from the queryset
            article_data2 = article_data.filter(description__icontains = query).exclude(title__icontains = query)
            article_data3 = article_data.filter(slug__icontains = query).exclude(Q(title__icontains = query) | Q(description__icontains = query))
            article_data4 = article_data.filter(Q(user__first_name__icontains = query) | Q(user__last_name__icontains = query)).exclude(Q(title__icontains = query) | Q(description__icontains = query) | Q(slug__icontains = query))
            
            article_final_data  = list(chain(article_data1, article_data2, article_data3, article_data4))
            
             
            lesson_data2 = lesson_data.filter(description__icontains = query)
            lesson_data3 = lesson_data.filter(slug__icontains = query).exclude(description__icontains =query)
            lesson_data4 = lesson_data.filter(summary__icontains = query).exclude(Q(description__icontains = query) | Q(slug__icontains = query))
            lesson_data5 = lesson_data.filter(Q(user__first_name__icontains = query) | Q(user__last_name__icontains = query)).exclude((Q(description__icontains = query) | Q(slug__icontains = query) | Q(summary__icontains = query)))
            
            lesson_final_data = list(chain(lesson_data2, lesson_data3, lesson_data4, lesson_data5))

            tutorial_data3 = tutorial_data.filter(slug__icontains = query)
            tutorial_data4 = tutorial_data.filter(author__icontains = query).exclude(slug__icontains =query)
            tutorial_data5 = tutorial_data.filter(Q(user__first_name__icontains = query) | Q(user__last_name__icontains = query)).exclude(Q(slug__icontains = query) | Q(author__icontains = query))
            tutorial_data1 = tutorial_data.filter(title__icontains = query).exclude(Q(slug__icontains = query) | Q(author__icontains = query))
            
            tutorial_final_data = list(chain(tutorial_data3, tutorial_data4, tutorial_data5, tutorial_data1))

            chapter_data4 = chapter_data.filter(author__icontains = query)
            chapter_data5 = tutorial_data.filter(Q(user__first_name__icontains = query) | Q(user__last_name__icontains = query))
            chapter_data1 = chapter_data.filter(title__icontains = query).exclude(author__icontains = query)
            chapter_data2 = chapter_data.filter(description__icontains = query).exclude(Q(author__icontains =query) | Q(title__icontains =query))
            
            chapter_final_data = list(chain(chapter_data4, chapter_data5, chapter_data1, chapter_data2))
            
            book_data5 = book_data.filter(Q(user__first_name__icontains = query) | Q(user__last_name__icontains = query))
            book_data1 = book_data.filter(title__icontains = query)
            book_data2 = book_data.filter(description__icontains = query).exclude(title__icontains =query)
            book_data3 = book_data.filter(isbn__icontains = query).exclude(Q(description__icontains =query) | Q(title__icontains = query))
            
            book_final_data = list(chain(book_data5, book_data1, book_data2, book_data3))


        """Serializing the Queryset"""
        serializer_article = ArticleSerializer(article_final_data, many=True)
        serializer_lesson = LessonSerializer(lesson_final_data, many = True)
        serializer_tutorial = TutorialSerializer(tutorial_final_data, many=True)
        serializer_chapter = ChapterSerializer(chapter_final_data, many = True)
        serializer_book = BookSerializer(book_final_data, many = True)   
        
        # Returning the serializers
        return Response({"Article":serializer_article.data,
                                "Lesson" :serializer_lesson.data,
                                "Tutorial": serializer_tutorial.data,
                                "Chapter": serializer_chapter.data,
                                "Book": serializer_book.data}, status=200)

@api_view(['GET'])   
def get_user(request):
    query = request.GET.get('query')

    new_queryset = []
    if query is not None:
        queryset = NewUser.objects.all()

        search_queryset1 = queryset.filter(first_name__icontains = query)
        search_queryset2 = queryset.filter(last_name__icontains = query)
        new_queryset= search_queryset1.union(search_queryset2)
        
    final_queryset = NewUserSerializer(new_queryset, many = True)
    return Response({"User":final_queryset.data})
 

def my_filter_fn(queryset, request):
    queryset = Article.objects.all()
    query = request.GET.get('query', None)
    if query is not None:
        article_data1 = queryset.filter(title__icontains = query)           
        article_data2 = queryset.filter(description__icontains = query).exclude(title__icontains = query)
        article_data3 = queryset.filter(slug__icontains = query).exclude(Q(title__icontains = query) | Q(description__icontains = query))
        article_data4 = queryset.filter(Q(user__first_name__icontains = query) | Q(user__last_name__icontains = query)).exclude(Q(title__icontains = query) | Q(description__icontains = query) | Q(slug__icontains = query))
                   
        queryset  = article_data1.union(article_data2, article_data3, article_data4)
    return queryset


def my_filter_fn1(queryset, request):
    queryset = Lesson.objects.all()
    query = request.GET.get('query', None)
    if query is not None:
        lesson_data2 = queryset.filter(description__icontains = query)           
        lesson_data3 = queryset.filter(slug__icontains = query).exclude(description__icontains = query)  
        lesson_data4 = queryset.filter(summary__icontains = query).exclude(Q(description__icontains = query) | Q(slug__icontains = query))
        lesson_data5 = queryset.filter(Q(user__first_name__icontains = query) | Q(user__last_name__icontains = query)).exclude((Q(description__icontains = query) | Q(slug__icontains = query) | Q(summary__icontains = query)))
     
        queryset  = lesson_data2.union(lesson_data3, lesson_data4, lesson_data4, lesson_data5)
    return queryset

def my_filter_fn2(queryset, request):
    queryset = Tutorial.objects.all()
    query = request.GET.get('query', None)
    if query is not None:
        tutorial_data3 = queryset.filter(slug__icontains = query)           
        tutorial_data4 = queryset.filter(author__icontains = query).exclude(title__icontains = query)     
        tutorial_data5 = queryset.filter(Q(user__first_name__icontains = query) | Q(user__last_name__icontains = query)).exclude(Q(slug__icontains = query) | Q(author__icontains = query))
        tutorial_data1 = queryset.filter(title__icontains = query).exclude(Q(slug__icontains = query) | Q(author__icontains = query))
  
        queryset  = tutorial_data3.union(tutorial_data4, tutorial_data5, tutorial_data1)
    return queryset

def my_filter_fn3(queryset, request):
    queryset = Chapter.objects.all()
    query = request.GET.get('query', None)
    if query is not None:
        chapter_data4 = queryset.filter(author__icontains = query)           
        chapter_data5 = queryset.filter(Q(user__first_name__icontains = query) | Q(user__last_name__icontains = query))
        chapter_data1 = queryset.filter(title__icontains = query).exclude(author__icontains = query)
        chapter_data2 = queryset.filter(description__icontains = query).exclude(Q(author__icontains =query) | Q(title__icontains =query))
     
        queryset  = chapter_data4.union(chapter_data5, chapter_data1, chapter_data2)
    return queryset

def my_filter_fn4(queryset, request):
    queryset = Book.objects.all()
    query = request.GET.get('query', None) 
    if query is not None:
        book_data5 = queryset.filter(Q(user__first_name__icontains = query) | Q(user__last_name__icontains = query))
        book_data1 = queryset.filter(title__icontains = query)
        book_data2 = queryset.filter(description__icontains = query).exclude(title__icontains =query)
        book_data3 = queryset.filter(isbn__icontains = query).exclude(Q(description__icontains =query) | Q(title__icontains = query))
        queryset  = book_data5.union(book_data1, book_data2, book_data3)
    return queryset

class IndexView(ObjectMultipleModelAPIView):
    querylist = [
        {'queryset': Article.objects.all(), 'serializer_class': ArticleSerializer, 'filter_fn': my_filter_fn},
        {'queryset': Lesson.objects.all(), 'serializer_class':LessonSerializer, 'filter_fn': my_filter_fn1},
        {'queryset': Tutorial.objects.all(), 'serializer_class':TutorialSerializer, 'filter_fn': my_filter_fn2},
        {'queryset': Chapter.objects.all(), 'serializer_class': ChapterSerializer, 'filter_fn': my_filter_fn3},
        {'queryset': Book.objects.all(), 'serializer_class': BookSerializer, 'filter_fn': my_filter_fn4}

        ]

   
        















