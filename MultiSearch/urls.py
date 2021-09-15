from django.urls import path
from .views import index, hello
app_name = 'MultiSearch'
urlpatterns = [
    path('myview/', index, name= 'index'),
    path('hello/', hello)
]
