from django.urls import path, include
from currency.views import (
    SourceListView,
    SourceCreateView,
    SourceUpdateView,
    SourceDeleteView,
    rates_view,
    contact_view,
    contact_us_list,
    source_details,
    source_delete,
)

urlpatterns = [
    path('rates/', rates_view, name='rates'),
    path("__debug__/", include("debug_toolbar.urls")),
    path('contact/', contact_view, name='contact'),
    path('contact-us/', contact_us_list, name='contact_us_list'),
    path('sources/', SourceListView.as_view(), name='source_list'),
    path('sources/details/<int:pk>/', source_details, name='source_details'),
    path('sources/create/', SourceCreateView.as_view(), name='source_create'),
    path('sources/update/<int:pk>/', SourceUpdateView.as_view(), name='source_update'),
    path('sources/delete/<int:pk>/', SourceDeleteView.as_view(), name='source_delete'),
]

