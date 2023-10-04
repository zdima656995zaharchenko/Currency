from django.urls import path, include
from rest_framework.routers import DefaultRouter
from currency.api.v1.views import RateListAPIView, RateCreateAPIView, RateDetailedAPIView, SourceListAPIView, \
    SourceDetailedAPIView, \
    SourceCreateAPIView, ContactUsListAPIView, ContactUsDetailedAPIView, ContactUsCreateAPIView, LogsDetailedAPIView, \
    LogsListAPIView

app_name = "currency_api"

router = DefaultRouter(trailing_slash=False)
# router.register("rates", RateViewSet, basename="rate")

urlpatterns = [
    path("", include(router.urls)),

    # Rate model endpoints
    path("rate/list", RateListAPIView.as_view(), name="rate-list"),
    path("rate/create/", RateCreateAPIView.as_view(), name="rate-create"),
    path("rate/<int:pk>/", RateDetailedAPIView.as_view(),
         name="rate-retrieve-update-destroy"),

    # Source model endpoints
    path("source/list", SourceListAPIView.as_view(), name="source-list"),
    path("source/create/", SourceCreateAPIView.as_view(), name="source-create"),
    path("source/<int:pk>/", SourceDetailedAPIView.as_view(),
         name="source-retrieve-update-destroy"),

    # ContactUs model endpoints
    path("contactus/list", ContactUsListAPIView.as_view(), name="contactus-list"),
    path("contactus/create/", ContactUsCreateAPIView.as_view(), name="contactus-create"),
    path("contactus/<int:pk>/", ContactUsDetailedAPIView.as_view(),
         name="contactus-retrieve-update-destroy"),

    # Logs model endpoints
    path("logs/list", LogsListAPIView.as_view(), name="logs-list"),
    path("logs/<int:pk>/", LogsDetailedAPIView.as_view(),
         name="logs-retrieve-update-destroy"),
]
