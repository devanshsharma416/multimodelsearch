import django_filters
from .models import Article, Lesson, Tutorial, Book, Chapter

class ArticleFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(field_name = 'title', lookup_expr = 'exact')
    class Meta:
        model = Article
        fields = {'title': ['icontains'], 'description': ['icontains']}


class LessonFilter(django_filters.FilterSet):
    class Meta:
        model = Lesson
        fields = {'description': ['icontains'], 'slug':['icontains']}

class TutorialFilter(django_filters.FilterSet):
    class Meta:
        model = Lesson
        fields = {'slug': ['icontains'], 'title': ['icontains']}