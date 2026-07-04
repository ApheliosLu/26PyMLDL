# Author: ApheliosLu
# 2026-07-03 20:22:35
# https://github.com/ApheliosLu


class Node:
    def __init__(self, elem=-1, lchild=None, rchild=None):
        self.elem = elem
        self.lchild = lchild
        self.rchild = rchild


class BinaryTree:
    def __init__(self):
        self.root = None
        self.auxiliary_queue = []  # 辅助队列

    def level_build_tree(self, node: Node):  # 层次建树
        if self.root is None:  # 树根为空
            self.root = node
            self.auxiliary_queue.append(node)  # 作为根结点入辅助队列
        else:
            self.auxiliary_queue.append(node)
            if self.auxiliary_queue[0].lchild is None:
                self.auxiliary_queue[0].lchild = node  # 放入左孩子
            else:
                self.auxiliary_queue[0].rchild = node  # 放入右孩子
                self.auxiliary_queue.pop(0)  # 当前节点的孩子节点都放完了，出队

    def pre_order(self, current_node: Node):  # 先序遍历，也即深度优先遍历
        if current_node:
            print(current_node.elem, end=" ")
            self.pre_order(current_node.lchild)
            self.pre_order(current_node.rchild)

    def in_order(self, current_node: Node):
        if current_node:
            self.in_order(current_node.lchild)
            print(current_node.elem, end=" ")
            self.in_order(current_node.rchild)

    def post_order(self, current_node: Node):
        if current_node:
            self.post_order(current_node.lchild)
            self.post_order(current_node.rchild)
            print(current_node.elem, end=" ")

    def level_order(self):  # 层序遍历
        help_queue = [
            self.root
        ]  # 用列表字面量一步完成初始化，等价于下面两行；系局部变量，没有使用self.auxiliary_queue
        # auxiliary_queue = []
        # auxiliary_queue.append(self.root)

        while help_queue:  # 队列非空
            out_node: Node = help_queue.pop(0)  # 队头出队
            print(out_node.elem, end=" ")
            if out_node.lchild:
                help_queue.append(out_node.lchild)  # 左孩子非空，左孩子入队
            if out_node.rchild:
                help_queue.append(out_node.rchild)


if __name__ == "__main__":
    tree = BinaryTree()
    for i in range(1, 11):
        new_node = Node(i)  # 实例化结点，层次建树
        tree.level_build_tree(new_node)

    print(f"队列实现层次遍历：")
    tree.level_order()
    print()

    print(f"递归实现先序遍历：")
    tree.pre_order(tree.root)
    print()

    print(f"递归实现中序遍历：")
    tree.in_order(tree.root)
    print()

    print(f"递归实现后序遍历：")
    tree.post_order(tree.root)
