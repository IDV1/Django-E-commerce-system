import datetime

from django.core.exceptions import ObjectDoesNotExist
from rest_framework.views import APIView

from apps.user.models import User
from apps.user.serialize import UserSerializer
from apps.utils.stauts import UserStatus

from apps.utils.user_password_encode import from_bcrypt


# 用户
class UserAPIView(APIView):
    # 请求前端json用户注册字段
    def post(self, request):
        user_request_get_password = request.data.get("password")
        request_all = request.data
        # 转换前端传来的密码进行加密计算
        request_all["password"] = from_bcrypt(user_request_get_password)
        request_all["create_time"] = datetime.datetime.now()
        # 反序列化
        user_deserialize = UserSerializer(data=request_all)
        user_deserialize.is_valid(raise_exception=True)
        user_deserialize.save()

        return UserStatus.success(user_deserialize.data)

    # 获取用户信息
    def get(self, request):
        get_email = request.GET.get("email")
        try:
            data = User.objects.get(email=get_email)
        except ObjectDoesNotExist:
            return UserStatus.failed("数据不存在")

        serializer = UserSerializer(instance=data)
        return UserStatus.success(serializer.data)
