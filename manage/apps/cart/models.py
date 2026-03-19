import json

from django.db import models

# 对应数据库shopping_cart
class ShoppingCart(models.Model):
    sku_id = models.CharField(max_length=255)
    nums = models.IntegerField()
    is_delete = models.IntegerField()
    email = models.CharField(max_length=255)
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shopping_cart'
