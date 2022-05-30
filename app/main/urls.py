from django.urls import path, include
from.views import index, about, index1, index2, index3, index4, index5
urlpatterns = [
    path('', index, name='index'),
    path('about', about, name='about'),
    path('index1', index1, name='index1'),
    path('index2', index2, name='index2'),
    path('index3', index3, name='index3'),
    path('index4', index4, name='index4'),
    path('index5', index5, name='index5'),
]
