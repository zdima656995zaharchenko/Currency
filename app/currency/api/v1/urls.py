from django.urls import path, include
from rest_framework.routers import DefaultRouter
from currency.api.v1.views import RateViewSet, RateDetailDestroyApiView

app_name = "currency_api"

router = DefaultRouter(trailing_slash=False)
router.register("rates", RateViewSet, basename="rate")

urlpatterns = [
    path("", include(router.urls)),
    path(
        "rates/detail-delete/<int:pk>/",
        RateDetailDestroyApiView.as_view(),
        name="rate-detail-delete",
    ),
]
