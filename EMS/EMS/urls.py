from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Home.urls')),
    path('users/',include('users.urls')),
    path('events/',include('events.urls')),
]