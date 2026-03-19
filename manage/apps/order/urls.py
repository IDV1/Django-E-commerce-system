from django.urls import path

from apps.order.views import OrderGenricAPI

urlpatterns = [
    path("goods/",OrderGenricAPI.as_view()),
]