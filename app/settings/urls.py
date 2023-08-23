from django.urls import path
from currency import views

urlpatterns = [
    path('rates/', views.rates_view, name='rates'),
    path('contact/', views.contact_view, name='contact'),
    path('contact-us/', views.contact_us_list, name='contact_us_list'),
    path('sources/', views.source_list, name='source_list'),
    path('sources/details/<int:pk>/', views.source_details, name='source_details'),
    path('sources/create/', views.source_create, name='source_create'),
    path('sources/update/<int:pk>/', views.source_update, name='source_update'),
    path('sources/delete/<int:pk>/', views.source_delete, name='source_delete'),
]
