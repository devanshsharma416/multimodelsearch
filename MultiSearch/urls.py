from django.urls import path
from .views import IndexView
from rest_framework.urlpatterns import format_suffix_patterns
app_name = 'MultiSearch'

urlpatterns = [
    path('', IndexView.as_view(), name= 'index'),
]
urlpatterns = format_suffix_patterns(urlpatterns)