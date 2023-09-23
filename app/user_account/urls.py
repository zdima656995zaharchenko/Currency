from django.urls import path

from user_account.views import SignUpView, UserActivateView

app_name = 'user_account'

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('activate/<uuid:username>', UserActivateView.as_view(), name='activate')
]