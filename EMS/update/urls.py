# update_user/urls.py
from django.urls import path
from .views import update

urlpatterns = [
    path('update/', update, name='update'),  # URL name matches here
]
