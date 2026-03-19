from rest_framework import serializers

from apps.order.models import Order

from apps.order.models import OrderGoods


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class OrderGoodsSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderGoods
        fields = '__all__'