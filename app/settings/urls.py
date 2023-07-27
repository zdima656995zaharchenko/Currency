# currency/urls.py
from django.urls import path
from currency import views

urlpatterns = [
    path('', views.contact_us_list, name='home'),
    path('contactus/list/', views.contact_us_list, name='contact_us_list'),
]
