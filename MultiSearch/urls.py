from django.urls import path
from .views import index
app_name = 'MultiSearch'
urlpatterns = [
    path('', index, name= 'index.html')
]
