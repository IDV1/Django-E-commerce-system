import json

from django.db import models

# 主菜单
class MainMenu(models.Model):
    main_menu_id = models.IntegerField()
    main_menu_name = models.CharField(max_length=255)
    main_menu_url = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'main_menu'

    # 手动序列化，使用魔术方法将所有映射字段转换成json格式
    def __str__(self):
        save_type = {}
        save_type['main_menu_id'] = self.main_menu_id
        save_type['main_menu_name'] = self.main_menu_name
        save_type['main_menu_url'] = self.main_menu_url

        return json.dumps(save_type, ensure_ascii=False)

# 二级菜单
class SubMenu(models.Model):
    main_menu_id = models.IntegerField(blank=True, null=True)
    sub_menu_id = models.IntegerField(blank=True, null=True)
    sub_menu_type = models.CharField(max_length=255, blank=True, null=True)
    sub_menu_name = models.CharField(max_length=255, blank=True, null=True)
    sub_menu_url = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sub_menu'

    def __str__(self):
        save_type = {}
        save_type['main_menu_id'] = self.main_menu_id
        save_type['sub_menu_id'] = self.sub_menu_id
        save_type['sub_menu_type'] = self.sub_menu_type
        save_type['sub_menu_name'] = self.sub_menu_name
        save_type['sub_menu_url'] = self.sub_menu_url

        return json.dumps(save_type, ensure_ascii=False)
