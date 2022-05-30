
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('about', include('main.urls')),
    path('index1', include('main.urls')),
    path('index2', include('main.urls')),
    path('index3', include('main.urls')),
    path('index4', include('main.urls')),
    path('index5', include('main.urls')),
    ]
