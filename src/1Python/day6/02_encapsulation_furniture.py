# Author: ApheliosLu
# 2026-06-14 14:02:48
# https://github.com/ApheliosLu


class HouseItem:
    def __init__(self, name, area):
        """
        家具初始化方法
        :param name: 家具名字
        :param area: 家具占地面积
        """
        self.name = name
        self.area = area

    def __str__(self):
        return f"{self.name}占地面积为{self.area:.2f}"


class House:
    def __init__(self, house_type, area):
        """
        房子初始化方法
        :param house_type: 户型
        :param area: 户型总面积
        """
        self.house_type = house_type
        self.area = area
        self.free_area = area  # 剩余可用面积，初始值为户型总面积area
        self.items_list = []  # 房子内的家具列表

    def __str__(self):
        return f"户型：{self.house_type}\n总面积:{self.area:.2f}[剩余：{self.free_area:.2f}]\n家具:{self.items_list}"

    def add_item(self, item: HouseItem):  # 通过冒号：对象类型，加类型注释
        if item.area > self.free_area:
            print(f"房子没空间了，放置家具失败！")
            return
        # 计算剩余面积
        self.free_area -= item.area
        # 将家具的名称追加到家具名称列表中
        self.items_list.append(item.name)


if __name__ == "__main__":
    bed = HouseItem("席梦思", 4)
    chest = HouseItem("衣柜", 2)
    table = HouseItem("餐桌", 1.5)
    print(bed)
    print(chest)
    print(table)

    print("-" * 50)
    house = House("两室一厅", 30)
    house.add_item(bed)
    house.add_item(chest)
    house.add_item(table)
    print(house)
