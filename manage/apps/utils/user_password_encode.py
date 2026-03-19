import hashlib

import bcrypt


# 用户密码转码
def from_bcrypt(value):
    return bcrypt.hashpw(value.encode("utf-8"),salt= bcrypt.gensalt(12)).decode("utf-8")