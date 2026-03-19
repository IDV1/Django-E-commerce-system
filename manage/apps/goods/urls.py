from django.urls import path

from apps.goods.views import GoodsDetailAPIView

from apps.goods.views import GoodsCategoryAPIView

urlpatterns = [
    path("category/<int:category_id>/<int:page>",GoodsCategoryAPIView.as_view()),
    path("<str:sku_id>", GoodsDetailAPIView.as_view()),
]