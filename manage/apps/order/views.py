from django.http import JsonResponse
from rest_framework.generics import GenericAPIView

from apps.order.models import Order
from apps.order.serializer import OrderGoodsSerializer


# 订单
class OrderGenricAPI(GenericAPIView):
    queryset = Order.objects
    serializer_class = OrderGoodsSerializer

    # 前端goods订单
    def post(self, request):
        request = request.data
        self.get_queryset()
        ser = self.get_serializer(data=request)
        ser.is_valid(raise_exception=True)
        ser.save()

        return JsonResponse(ser.data, safe=False)

    # 拿到order/goods全部订单
    def get(self, request):
        queryset = self.get_queryset()
        ser = self.get_serializer(queryset, many=True)
        return JsonResponse(ser.data, safe=False)

