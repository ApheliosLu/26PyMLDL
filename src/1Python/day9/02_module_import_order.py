# Author: ApheliosLu
# 2026-07-13 09:58:56
# https://github.com/ApheliosLu

# import sys
#
# import module.my_module
#
# module.my_module.test1()
#
# print(sys.path)
# 上述代码可直接运行：以常见的导入包中的文件并运行文件中的函数的方式


# 另一种运行方式：程序执行时添加新的模块路径，而非导入包
import sys

# sys.path.append("module")  # 将module包加入文件执行搜索路径（末尾），此时 module 不再被当成 “包”，只是一个普通搜索目录。
sys.path.insert(0, "module")  # 将module包加入文件执行搜索路径（首位）
print(sys.path)
print("-" * 50)

import my_module  # 可直接导入module包下的模块

my_module.test1()
