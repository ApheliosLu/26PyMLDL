# Author: ApheliosLu
# 2026-06-15 15:02:11
# https://github.com/ApheliosLu


class A:
    def test(self):
        print(f"A test")

    def demo(self):
        print(f"A demo")


class B:
    def test(self):
        print(f"B test")

    def demo(self):
        print(f"B demo")


class C(B, A):
    def test(self):
        print(f"C test")


if __name__ == "__main__":
    c = C()
    c.test()
    print(C.__mro__)  # method resolution order
