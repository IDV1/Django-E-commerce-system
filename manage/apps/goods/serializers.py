from rest_framework import serializers

from manage.settings import IMAGE_URL

from apps.goods.models import Goods


class GoodsDetailSerializer(serializers.ModelSerializer):
    # 自定义
    image_url = serializers.SerializerMethodField()
    # 格式化时间字段
    create_time = serializers.DateTimeField("%Y-%m-%d %H:%M:%S")
    # 图片序列化
    def get_image_url(self, obj):
        image = IMAGE_URL + obj.image
        return image

    class Meta:
        model = Goods
        fields = '__all__'
