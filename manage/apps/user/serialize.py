from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from apps.user.models import User


class UserSerializer(serializers.ModelSerializer):
    # 使用邮箱作为用户的登录接口
    email = serializers.EmailField(
        required=True,
        allow_blank=False,
        # 唯一性验证
        validators=[UniqueValidator(
            queryset=User.objects.all(),
            message="Email already exists"
        )]
    )
    # 序列化生日
    birthday = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", input_formats=["%Y-%m-%d %H:%M:%S"])
    # 创建时间序列化
    create_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", input_formats=["%Y-%m-%d %H:%M:%S"])

    class Meta:
        model = User
        fields = "__all__"