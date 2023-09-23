from django.contrib import admin
from django.urls import path, include
from django.urls import re_path
from currency.views import ProfileView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("auth/", include("django.contrib.auth.urls")),
    path("", include("currency.urls")),
    path('auth/profile/<int:pk>/', ProfileView.as_view(), name='profile'),
    path('user/account/', include('user_account.urls')),
    path('login/', auth_views.LoginView.as_view(), name='login'),
]