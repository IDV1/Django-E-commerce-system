import json
from decimal import Decimal

# 解决Decimal 类型
class FromDecimal(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return float(obj)
