from rest_framework import serializers
from .models import Article, Lesson, NewUser, Tutorial, Book, Chapter


"""Creating Class Based Serializers"""
class NewUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewUser
        fields = ('first_name', 'last_name', 'username', 'date_joined')


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('title', 'description', 'slug', 'user', 'summary')


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"


class TutorialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tutorial
        fields = "__all__"


class ChapterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chapter
        fields = "__all__"

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"


# class ArticleSerializer(serializers.Serializer):
#     title = serializers.CharField(required = False, allow_blank=True, max_length = 20)
#     description = serializers.CharField(style = {'base_template': 'textarea.html'}, required = False, allow_blank = True, max_length = 200)
#     slug = serializers.SlugField(required = False)
#     featured = serializers.BooleanField(default = False, required = False)
#     publish_date  = serializers.DateTimeField(format=api_settings.DATETIME_FORMAT, input_formats=None, default_timezone=None, required = False)

#     def create(self, validate_data):
#         '''Create and return the new Article intance, givent the validate data'''
#         return Article.objects.create(**validate_data)

#     def update(self, instance, validate_data):
#         '''Update and return an existing `Snippet` instance, given the validated data.'''
#         instance.title = validate_data.get('title', instance.title)
#         instance.description = validate_data.get('description', instance.description)
#         instance.slug = validate_data.get('slug', instance.slug)
#         instance.featured = validate_data.get('featured', instance.featured)
#         instance.publish_date = validate_data.get('publish_date', instance.publish_date )

#         instance.save()
#         return instance


# class LessonSerializer(serializers.Serializer):
#     title = serializers.CharField(required = False, allow_blank=True, max_length = 20)
#     description = serializers.CharField(style = {'base_template': 'textarea.html'}, required = False, allow_blank = True, max_length = 200)
#     slug = serializers.SlugField(required = False)
#     featured = serializers.BooleanField(default = False, required = False)
#     publish_date  = serializers.DateTimeField(format=api_settings.DATETIME_FORMAT, input_formats=None, default_timezone=None)


#     def create(self, validate_data):
#         '''Create and return the new Article intance, givent the validate data'''
#         return Lesson.objects.create(**validate_data)

#     def update(self, instance, validate_data):
#         '''Update and return an existing `Snippet` instance, given the validated data.'''
#         instance.title = validate_data.get('title', instance.title)
#         instance.description = validate_data.get('description', instance.description)
#         instance.slug = validate_data.get('slug', instance.slug)
#         instance.featured = validate_data.get('featured', instance.featured)
#         instance.publish_date = validate_data.get('publish_date', instance.publish_date)

#         instance.save()
#         return instance

# class TutorialSerializer(serializers.Serializer):
#     title = serializers.CharField(required = False, allow_blank=True, max_length = 20)
#     description = serializers.CharField(style = {'base_template': 'textarea.html'}, required = False, allow_blank = True, max_length = 200)
#     slug = serializers.SlugField(required = False)
#     author = serializers.CharField(required = False)
#     featured = serializers.BooleanField(default = False, required = False)
#     publish_date  = serializers.DateTimeField(format=api_settings.DATETIME_FORMAT, input_formats=None, default_timezone=None)

#     def create(self, validate_data):
#         '''Create and return the new Article intance, givent the validate data'''
#         return Tutorial.objects.create(**validate_data)

#     def update(self, instance, validate_data):
#         '''Update and return an existing `Snippet` instance, given the validated data.'''
#         instance.title = validate_data.get('title', instance.title)
#         instance.description = validate_data.get('description', instance.description)
#         instance.slug = validate_data.get('slug', instance.slug)
#         instance.author = validate_data.get('author', instance.author)
#         instance.featured = validate_data.get('featured', instance.featured)
#         instance.publish_date = validate_data.get('publish_date', instance.publish_date )
#         instance.save()
#         return instance

