from rest_framework.views import APIView

from apps.cart.models import ShoppingCart

from apps.utils.stauts import CartStatus

from apps.cart.deserial import CartSerializer


# 购物车接口
#/cart/
class CartAPIView(APIView):
    def post(self, request):
        # @ 后续补充用户认证
        ## 假设前端传入
        # {
        #     "username": "1@qq.com",
        #     "sku_id": 11020030,
        #     "email": "1@qq.com",
        #     "nums": 2,
        #     "is_delete": 0
        # }

        # 前端请求数据信息
        global get_exists_data
        get_data = request.data
        # 拿到前端请求信息
        get_email = get_data.get("email")
        # 商品id
        get_sku_id = get_data.get("sku_id")
        # 数量
        get_nums = get_data.get("nums")
        is_delete = get_data.get("is_delete")

        # 到数据库里找存在字段
        get_filter_data = ShoppingCart.objects.filter(
            sku_id=get_sku_id,
            email= get_email,
            is_delete = 0 # 拿到没删除的
        )

        # 存在拿到数据
        if get_filter_data.exists():
            # 拿到数据库里筛选的字段
            get_exists_data = get_filter_data.get()
            if is_delete == 0:
                # 更新值
                update_nums = get_nums + get_exists_data.nums
                get_data["nums"] = update_nums

            elif is_delete == 1:
                get_data["nums"] = get_exists_data.nums

            deserialized_data = CartSerializer(data=get_data)
            deserialized_data.is_valid(raise_exception=True)

            # 更新
            get_filter_data.update(**deserialized_data.data)

            if is_delete == 0:
                return CartStatus.success("数据更新成功")
            elif is_delete == 1:
                return CartStatus.success("数据删除成功")

        else:
            # 反序列
            deserialized_data = CartSerializer(data=get_data)
            deserialized_data.is_valid(raise_exception=True)

            ShoppingCart.objects.create(**deserialized_data.data)

            return CartStatus.success("数据插入成功")

    # /cart?email=1020@cnm.com
    def get(self, request):
        get_url_email = request.GET.get("email")
        cart_result = ShoppingCart.objects.filter(email=get_url_email)
        cart_serializer = CartSerializer(instance=cart_result, many=True)
        return CartStatus.success(cart_serializer.data)
