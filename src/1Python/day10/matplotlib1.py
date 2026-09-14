# 由matplotlib1.ipynb转换而来
# %%
# %%
# 定义一个变量
a = 5
# %%
# %% [markdown]
# 这个是注释
# %%
b = 5
# %%
# %%
b += 3
# %%
# %%
b += 3
# %%
# %%
import random

print(random.randint(1, 10))

from matplotlib import pyplot as plt
import matplotlib

matplotlib.use("Agg")  # 使用无图形界面的后端
plt.plot([1, 0, 9], [4, 5, 6])

# plt.show()  # py文件不能像ipynb文件一样去show
plt.savefig("test.png")
