from apps.address.views import AddressGenricAPI
from django.urls import path, re_path

from apps.address.views import AddressList

urlpatterns = [
    path("",AddressGenricAPI.as_view()),
    path("goods/<int:id>",AddressGenricAPI.as_view()),
    path("list/",AddressList.as_view())
]