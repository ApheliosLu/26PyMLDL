# Author: ApheliosLu
# 2026-06-14 14:34:22
# https://github.com/ApheliosLu


class Gun:
    def __init__(self, model):
        self.model = model
        self.bullet_count = 0

    def add_bullet(self, count):
        self.bullet_count += count

    def shoot(self):
        if self.bullet_count <= 0:
            print(f"{self.model}没有子弹了……")
            return
        self.bullet_count -= 1
        print(f"{self.model}发射子弹,子弹剩余{self.bullet_count}")


class Soldier:
    def __init__(self, name, gun: Gun = None):
        self.name = name
        self.gun = gun

    def fire(self):
        if self.gun is None:
            print(f"{self.name}还没有枪……")
            return
        print(f"{self.name}冲啊！！！")
        self.gun.add_bullet(50)
        self.gun.shoot()


if __name__ == "__main__":
    ak47 = Gun("Ak47")
    ak47.add_bullet(50)
    ak47.shoot()

    xusanduo = Soldier("许三多")
    xusanduo.fire()

    xusanduo.gun = ak47
    xusanduo.fire()
    xusanduo.fire()
