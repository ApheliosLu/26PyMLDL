# Author: ApheliosLu
# 2026-06-22 21:04:12
# https://github.com/ApheliosLu

import random
from module1 import test1
from module2 import test1 as module2_test1

print(random.__file__)  # 查看模块所在路径
a = random.randint(1, 3)
print(a)

test1()  # 后导入的模块的同名函数会覆盖先导入的模块的同名函数
module2_test1()
