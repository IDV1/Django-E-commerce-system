from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, \
    ListModelMixin

from apps.address.models import UserAddress

from apps.address.serialize import UserAddressSerializer


# 用户地址
class AddressGenricAPI(GenericAPIView,
                       CreateModelMixin,
                       RetrieveModelMixin,
                       UpdateModelMixin,
                       DestroyModelMixin):
    queryset = UserAddress.objects
    serializer_class = UserAddressSerializer
    # 默认是pk，设置为自定id
    lookup_field = "id"
    # 前端json请求
    def post(self,request):
        # 插入请求数据
        return self.create(request)

    # address/goods/6 查询id=6的商品地址
    def get(self,request,id):
        # 序列化
        return self.retrieve(request)

    # 修改id
    def put(self,request,id):
        try:
            self.update(request,id)
            return JsonResponse({"code": 200, "msg": "修改成功"})
        except Exception:
            return JsonResponse({"code": 1001, "msg": "修改失败"})


    # 删除id
    def delete(self,request,id):
        try:
            self.destroy(request, id)
            return JsonResponse({"code": 200, "msg": "删除成功"})
        except Exception:
            return JsonResponse({"code": 1001, "msg": "删除失败"})

class AddressList(ListModelMixin,GenericAPIView):
    queryset = UserAddress.objects
    serializer_class = UserAddressSerializer

    def get(self,request):
        return self.list(request)
