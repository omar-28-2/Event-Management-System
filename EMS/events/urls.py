from django.urls import path
from . import views

urlpatterns = [
    path('events_list/', views.events_list, name='events_list'),
    path('request_form/', views.request_form, name='request_form'),
    path('vendor_event_submit/', views.vendor_event_submit, name='vendor_event_submit'),
]