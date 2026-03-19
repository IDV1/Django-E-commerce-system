from rest_framework import serializers

from apps.cart.models import ShoppingCart


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoppingCart
        fields = "__all__"
