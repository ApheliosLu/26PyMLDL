# Author: ApheliosLu
# 2026-06-19 14:48:34
# https://github.com/ApheliosLu


class MusicPlayer(object):
    instance = None
    init_flag = False

    def __new__(cls, *args, **kwargs):
        # 单例模式：只为第一个对象分配空间
        if cls.instance is None:
            cls.instance = super().__new__(cls)  # 父类的new 类似于c的malloc：分配空间
            print(f"创建对象，分配空间！")
        return cls.instance  # 返回类属性保存的对象引用

    def __init__(self, name):
        self.name = name
        if not MusicPlayer.init_flag:  # 场景：让初始化动作只执行一次
            print(f"初始化音乐播放器！")
            MusicPlayer.init_flag = True


if __name__ == "__main__":
    player1 = MusicPlayer("七里香")
    player2 = MusicPlayer("东风破")
    print(id(player1))  # 两者id相同
    print(id(player2))
    print(player1.name)  # 东风破
    print(player2.name)  # 东风破
