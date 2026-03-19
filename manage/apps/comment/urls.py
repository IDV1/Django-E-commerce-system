from django.urls import path

from comment.views import CommentView

urlpatterns = [
    # 使用viewsetMixmin来解决单个路由的问题
    path("",CommentView.as_view({
        '''拿全部'''
        "get": "get_all",
        "post": "insert"
    })),
    path("<int:id>",CommentView.as_view({
        '''拿id为x的'''
        "get": "single",
        "put": "update_data",
        "delete": "delete"
    }))
]