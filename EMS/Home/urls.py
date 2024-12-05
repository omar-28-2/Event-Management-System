from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('submit-contact-form/', views.contactForm, name='contactForm'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
]
