from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, \
    ListModelMixin

from apps.comment.models import Comment

from comment.serialize import CommentSerializer
from rest_framework.viewsets import ViewSetMixin


# 评论
class CommentView(ViewSetMixin,
                  GenericAPIView,
                  CreateModelMixin,
                  RetrieveModelMixin,
                  UpdateModelMixin,
                  DestroyModelMixin,
                  ListModelMixin):
    queryset = Comment.objects
    serializer_class = CommentSerializer
    lookup_field = "id"

    # 拿到所有数据
    def get_all(self,request):
        return self.list(request)

    # 拿到id为x的数据
    def single(self,request,id):
        return self.retrieve(request)

    # 插入数据
    def insert(self,request):
        return self.create(request)

    # 修改数据
    def update_data(self,request,id):
        return self.update(request)

    # 删除数据
    def delete(self,request,id):
        return self.destroy(request,id)
