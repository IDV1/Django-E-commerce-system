from rest_framework.views import APIView

from apps.goods.models import Goods
from apps.utils.stauts import GoodsStatus

from apps.goods.serializers import GoodsDetailSerializer


# 商品分类接口
class GoodsCategoryAPIView(APIView):
    # goods/category/1/2
    def get(self, request, category_id, page):
        #
        current_page = (page-1)*20
        end_page = page*20
        category_data = Goods.objects.filter(id=category_id).all()
        get_data = category_data[current_page:end_page]

        result_list = []
        for data in get_data:
            result_list.append(data.__str__())

        return GoodsStatus.success(data=result_list)

# 商品详细接口
class GoodsDetailAPIView(APIView):
    # goods/65542010588
    def get(self, request, sku_id):
        print(sku_id)
        get_sku_id = Goods.objects.filter(sku_id=sku_id).first()
        # 序列化instance 反data
        serializer = GoodsDetailSerializer(instance=get_sku_id).data

        return GoodsStatus.success(serializer)