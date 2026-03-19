import json
from django.http import HttpResponse

# 菜单状态码
class MenuStatus():
    @staticmethod
    def success(data):
        return HttpResponse(json.dumps({
            "status": 1000,
            "msg": "success",
            "data": data
        }), content_type="application/json")

    @staticmethod
    def failed(data):
        return HttpResponse(json.dumps({
            "status": 1001,
            "msg": "failed",
            "data": data
        }), content_type="application/json")

    @staticmethod
    def unknown(data):
        return HttpResponse(json.dumps({
            "status": 1002,
            "msg": "unknown?",
            "data": data
        }), content_type="application/json")

# 商品，2开头
class GoodsStatus():
    @staticmethod
    def success(data):
        return HttpResponse(json.dumps({
            "status": 2000,
            "msg": "success",
            "data": data
        }), content_type="application/json")

    @staticmethod
    def failed(data):
        return HttpResponse(json.dumps({
            "status": 2001,
            "msg": "failed",
            "data": data
        }), content_type="application/json")

    @staticmethod
    def unknown(data):
        return HttpResponse(json.dumps({
            "status": 2002,
            "msg": "unknown?",
            "data": data
        }), content_type="application/json")

# Shopping Cart header 3
class CartStatus():
    @staticmethod
    def success(data):
        return HttpResponse(json.dumps({
            "status": 3000,
            "msg": "success",
            "data": data
        }), content_type="application/json")

    @staticmethod
    def failed(data):
        return HttpResponse(json.dumps({
            "status": 3001,
            "msg": "failed",
            "data": data
        }), content_type="application/json")

    @staticmethod
    def unknown(data):
        return HttpResponse(json.dumps({
            "status": 3002,
            "msg": "unknown?",
            "data": data
        }), content_type="application/json")

# User header 4
class UserStatus():
    @staticmethod
    def success(data):
        return HttpResponse(json.dumps({
            "status": 4000,
            "msg": "success",
            "data": data
        }), content_type="application/json")

    @staticmethod
    def failed(data):
        return HttpResponse(json.dumps({
            "status": 4001,
            "msg": "failed",
            "data": data
        }), content_type="application/json")

    @staticmethod
    def unknown(data):
        return HttpResponse(json.dumps({
            "status": 4002,
            "msg": "unknown?",
            "data": data
        }), content_type="application/json")


