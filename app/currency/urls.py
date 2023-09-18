from django.urls import path, include
from django.contrib import admin
from currency import views
from django.contrib.auth import views as auth_views

from currency.views import (
    SourceListView,
    SourceCreateView,
    SourceUpdateView,
    SourceDeleteView,
    contact_view,
    contact_us_list,
    source_details,
    source_delete,
    ContactUsCreateView,
    IndexView,
    SupportForm,
    RateListView,
    RateCreateView,
    RateUpdateView,
    RateDeleteView,
    RateDetailView,
)


urlpatterns = [
    path('rates/', RateListView.as_view(), name='rate_list'),
    path('rates/create/', RateCreateView.as_view(), name='rate_create'),
    path('rates/update/<int:pk>/', RateUpdateView.as_view(), name='rate_update'),
    path('rates/delete/<int:pk>/', RateDeleteView.as_view(), name='rate_delete'),
    path('rates/details/<int:pk>/', RateDetailView.as_view(), name='rate_details'),
    path("__debug__/", include("debug_toolbar.urls")),
    path('contact/', contact_view, name='contact'),
    path('contact-us/', contact_us_list, name='contact_us_list'),
    path('sources/', SourceListView.as_view(), name='source_list'),
    path('sources/details/<int:pk>/', source_details, name='source_details'),
    path('sources/create/', SourceCreateView.as_view(), name='source_create'),
    path('sources/update/<int:pk>/', SourceUpdateView.as_view(), name='source_update'),
    path('sources/delete/<int:pk>/', SourceDeleteView.as_view(), name='source_delete'),
    path('contactus/create/', ContactUsCreateView.as_view(), name='contactus_create'),
    path('', IndexView.as_view(), name='index'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('change_password/', views.change_password, name='change_password'),
]
