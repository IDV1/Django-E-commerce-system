from django.http import HttpResponse
from django.views import View
from apps.menu.models import MainMenu
from apps.menu.models import SubMenu

from apps.utils.stauts import MenuStatus


# 一级菜单
class GoodsMainMenuView(View):
    def get(self, request):
        print("这是get")
        # 获取模块层数据库对应的全部数据,已被序列化的json数据
        # database_table = main_menu
        get_table_all = MainMenu.objects.all()

        result_list = []
        for i in get_table_all:
            result_list.append(i.__str__())

        return MenuStatus.success(data=result_list)

    def post(self, request):
        print("post")
        return HttpResponse("Goods Main Menu Post 的请求")

# 二级菜单
class GoodsSubMenuView(View):
    def get(self, request):
        # 拿到二级菜单关联的主菜单id参数
        get_main_menu_id = request.GET.get("main_menu_id")
        # 过滤条件，根据主菜单id拿到二级内容
        sub_menu = SubMenu.objects.filter(filter_main_menu_id=get_main_menu_id)

        result_list = []
        for i in sub_menu:
            result_list.append(i.__str__())

        return MenuStatus.success(data=result_list)

