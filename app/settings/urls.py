from django.contrib import admin
from django.urls import path, include
from currency import urls as currency_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(currency_urls)),
]
