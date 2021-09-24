from django.urls import path
from .views import IndexView, get_user
from rest_framework.urlpatterns import format_suffix_patterns
app_name = 'MultiSearch'

urlpatterns = [
    path('', IndexView.as_view(), name= 'index'),
    path('user/', get_user, name = "user")
]
urlpatterns = format_suffix_patterns(urlpatterns)