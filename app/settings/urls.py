# currency/urls.py
from django.urls import path
from currency import views

urlpatterns = [

    path('rates/', views.rates_view, name='rates'),
    path('contact/', views.contact_view, name='contact'),
    path('contact-us/', views.contact_us_list, name='contact_us_list'),
]
