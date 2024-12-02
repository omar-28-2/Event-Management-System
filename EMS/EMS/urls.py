from django.contrib import admin
from django.urls import path, include  # Include is required to link app urls

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin URL
    path('', include('Home.urls')),  # Link Home app to the root URL
]
