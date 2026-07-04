# Author: ApheliosLu
# 2026-07-04 11:47:37
# https://github.com/ApheliosLu

my_list = "This is a test string from Andrew".split()
print(my_list)
print("-" * 50)


def change_lower(str_name: str):
    return str_name.lower()


# key可以传递一个定义比较规则的函数
print(sorted(my_list, key=change_lower))  # sorted返回一个排序后的列表，不会改变原本列表
print("-" * 50)

# sort将改变原列表
my_list.sort(key=change_lower)
print(my_list)
print("-" * 50)

student_tuples = [("jane", "B", 12), ("john", "A", 15), ("dave", "B", 10)]

# lambda表达式（匿名函数）：提高编写效率、提高阅读速度
print(sorted(student_tuples, key=lambda x: x[2]))
print("-" * 50)


class Student:
    def __init__(self, name: str, grade, age: int):
        self.name = name
        self.grade = grade
        self.age = age

    def __repr__(self):
        """
        相对于__str__来说，更方便，可以返回非字符串类型
        :return:
        """
        return repr((self.name, self.grade, self.age))


student = Student("john", "A", 15)
student_objects = [
    Student("jane", "B", 12),
    Student("john", "A", 15),
    Student("dave", "B", 10),
]
print(sorted(student_objects, key=lambda stu: stu.age))
print("-" * 50)


from operator import itemgetter, attrgetter

print("使用operator系列：")
print(sorted(student_tuples, key=itemgetter(0)))
print(sorted(student_objects, key=attrgetter("age"), reverse=True))

print("使用operator系列，多列排序：")
print(sorted(student_tuples, key=itemgetter(1, 2)))
print(sorted(student_tuples, key=lambda x: (x[1], -x[2])))  # 第一列升序第二列降序
print(sorted(student_objects, key=attrgetter("grade", "age"), reverse=True))

print("查看排序稳定性：")
data = [("red", 1), ("blue", 1), ("red", 2), ("blue", 2)]
print(sorted(data, key=itemgetter(0)))
print("-" * 50)

my_dict = {
    "Li": ["M", 7],
    "Zhang": ["E", 2],
    "Wang": ["P", 3],
    "Du": ["C", 2],
    "Ma": ["C", 9],
    "Zhe": ["H", 7],
}
print(sorted(my_dict.items(), key=lambda x: x[1][1]))
print("-" * 50)

game_result = [
    {"name": "Bob", "wins": 10, "lossess": 3, "rating": 75.00},
    {"name": "David", "wins": 3, "lossess": 5, "rating": 57.00},
    {"name": "Carol", "wins": 4, "lossess": 5, "rating": 57.00},
    {"name": "Patty", "wins": 9, "lossess": 3, "rating": 71.48},
]
print(sorted(game_result, key=lambda x: x["rating"]))
print(sorted(game_result, key=itemgetter("rating", "name")))
