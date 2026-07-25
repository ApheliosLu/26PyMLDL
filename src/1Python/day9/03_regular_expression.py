# Author: ApheliosLu
# 2026-07-13 09:59:18
# https://github.com/ApheliosLu

import re


def use_simple():
    """
    初识re match group
    :return:
    """
    result = re.match("wangdao", "wangdao.cn")
    print(result)  # <re.Match object; span=(0, 7), match='wangdao'> 匹配不到则为None
    # 先判断不为None再调用group
    if result:
        print(result.group())  # wangdao


def use_single():
    """
    匹配单个字符
    :return:
    """
    if ret := re.match(".", "M"):  # 海象运算符 := 赋值并判断
        print(ret.group())

    if ret := re.match("t.o", "too"):
        print(ret.group())

    if ret := re.match("t.o", "two"):
        print(ret.group())

    print("-" * 100)

    # [] 匹配括号内列出的字符
    # 大小写h都可以的情况
    if ret := re.match("[hH]", "hello Python"):
        print(ret.group())

    if ret := re.match("[hH]", "Hello Python"):
        print(ret.group())

    if ret := re.match("[hH]ello Python", "hello Python"):
        print(ret.group())

    # 匹配0到9 或直接用\d
    if ret := re.match("[0-9]Hello Python", "6Hello Python"):
        print(ret.group())

    # 匹配0到3 5到9
    if ret := re.match("[0-35-9]Hello Python", "7Hello Python"):
        print(ret.group())

    print("-" * 100)

    # 使用\d进行匹配数字
    if ret := re.match(r"嫦娥\d号", "嫦娥1号发射成功"):  # 去掉r则：无效的转义序列\d
        print(ret.group())

    if ret := re.match(r"嫦娥\d号", "嫦娥2号发射成功"):
        print(ret.group())

    if ret := re.match(r"嫦娥\d号", "嫦娥3号发射成功"):
        print(ret.group())


def use_multiple():
    """
    匹配多个字符
    :return:
    """
    # * 0次或无数次
    # 匹配需求：一个字符串第一个字母为大写字符，后面都是小写字母并且这些小写字母可有可无
    if ret := re.match("[A-Z][a-z]*", "M"):
        print(ret.group())

    if ret := re.match("[A-Z][a-z]*", "MnnM"):
        print(ret.group())

    if ret := re.match("[A-Z][a-z]*", "Aabcdef"):
        print(ret.group())

    print("-" * 100)

    # + 1次或无数次
    # 匹配需求：变量名是否有效
    names = ["name1", "_name", "2_name", "__name__"]
    for name in names:
        if ret := re.match(r"[a-zA-Z_]+\w*", name):
            print(f"{ret.group()}是正确的！")
        else:
            print(f"{name}不符合命名规范！")

    print("-" * 100)

    # ? 1次或0次
    # 需求：匹配出，0 到 99 之间的数字
    if ret := re.match("[1-9]?[0-9]", "7"):
        print(ret.group())

    if ret := re.match(r"[1-9]?\d", "33"):
        print(ret.group())

    if ret := re.match(r"[1-9]?\d", "09"):  # 匹配0，并非想要的结果
        print(ret.group())

    print("-" * 100)

    # {m} {m,n} 指定匹配次数
    # 需求：匹配出，8 到 20 位的密码，可以是大小写英文字母、数字、下划线
    if ret := re.match("[a-zA-Z0-9_]{6}", "12a3g45678"):  # 必须匹配6个，否则匹配失败
        print(ret.group())

    if ret := re.match("[a-zA-Z0-9_]{8,20}", "1ad12f23s*34455ff66"):  # 匹配9位（贪婪）
        print(ret.group())

    # 需求：匹配出 163 的邮箱地址，且@符号之前有 4 到 20 位，例如hello@163.com
    if ret := re.match("[a-zA-Z0-9]{4,20}@163.com", "hello@163.com"):
        print(ret.group())


def start_end():
    """
    匹配 开头^ 结尾$
    :return:
    """
    # $ 结尾
    # 需求：匹配复合163的邮箱
    email_list = [
        "xiaoWang@163.com",
        "xiaoWang@163.comheihei",
        ".com.xiaowang@qq.com",
    ]
    for email in email_list:
        if ret := re.match(r"\w{4,20}@163\.com$", email):  # \.转义
            print(f"{email}是正确的邮箱！匹配后的结果是：{ret.group()}!")
        else:
            print(f"{email}不是正确的邮箱！")

    print("-" * 100)

    # 改进后的匹配0到99
    if ret := re.match(r"[1-9]?\d$", "09"):  # 匹配0，并非想要的结果
        print(ret.group())
    else:
        print(f"不是0到99之间！")


def split_group():
    """
    匹配分组
    | 匹配左右任意一个表达式（前面的先匹配）
    (ab) 将括号中字符作为一个分组
    \num 引用分组 num 匹配到的字符串
    (?P<name>) 分组起别名
    (?P=name) 引用别名为 name 分组匹配到的字符串
    :return:
    """
    # 匹配0到100
    if ret := re.match(r"[1-9]?\d$|100", "100"):
        print(ret.group())
    else:
        print(f"不是0到100之间！")
    print("-" * 100)

    # 匹配1到99,匹配分组、依次匹配、写到前面的先匹配
    if ret := re.match(r"[1-9][0-9]|[1-9]", "10"):
        print(ret.group())
    else:
        print(f"不是1到99之间！")
    print("-" * 100)

    # 匹配163、126、qq邮箱
    if ret := re.match(r"\w{4,20}@(163|126|qq)\.com", "test@qq.com"):
        print(ret.group())  # test@126.com
    print("-" * 100)

    # 不是以4 7 结尾的电话号码
    tels = ["13100001234", "18912344321", "10086", "18800007777"]
    for tel in tels:
        if ret := re.match(r"1\d{9}[0-35-68-9]$", tel):
            print(ret.group())
        else:
            print(f"{tel}不是想要的手机号！")
    print("-" * 100)

    # 提取区号和电话号码
    # [^-] 匹配任何非-的字符
    if ret := re.match(r"([^-]+)-(\d+)", "010-12345678"):
        print(ret.group())
        print(ret.group(1))  # 分组匹配后的第一组 010
        print(ret.group(2))  # 12345678
    print("-" * 100)

    # \num
    # 匹配一个引用分组 如果在第一对<>中是什么，按理说在后面的那对<>中就应该是什么
    # 比如只能匹配前面是html后面是/html，若后面是htmla则匹配失败
    # 用于爬虫网页数据
    # 错误版本：无捕获组，无法反向引用
    print("===== 无分组版本 =====")
    if ret := re.match(r"<[a-zA-Z]*>\w*</[a-zA-Z]*>", "<html>hh</htmla>"):
        print(ret.group())
    else:
        print(f"{ret}匹配失败！")
    print("-" * 100)
    # 正确版本1：原始字符串 + 捕获分组() + 反向引用\1
    print("===== 反向引用正确版本 =====")
    # ([a-zA-Z]*) 括号捕获标签名，后面用 \1 复用
    pattern = r"<([a-zA-Z]*)>\w*</\1>"
    if ret := re.match(pattern, "<html>hh</htmla>"):
        print(ret.group())
    else:
        print("<html>hh</htmla>是一对错误的标签！")
    # 测试正确标签 <div>test</div>
    if ret := re.match(pattern, "<div>test</div>"):
        print("正确匹配：", ret.group())
    print("-" * 100)

    # \number 匹配多个引用分组
    labels = [
        "<html><h1>www.cskaoyan.com</h1></html>",
        "<html><h1>www.cskaoyan.com</h2></html>",
    ]
    for label in labels:
        if ret := re.match(r"<(\w*)><(\w*).*</\2></\1>", label):
            print(f"{ret.group()}是符合要求的标签！")
        else:
            print(f"{label}不符合要求！")
    print("-" * 100)

    # 使用(?P<name>)和(?P=name)代替\num匹配引用分组
    for label in labels:
        if ret := re.match(
            r"<(?P<name1>\w*)><(?P<name2>\w*)>.*</(?P=name2)></(?P=name1)>", label
        ):
            print(ret.group())
        else:
            print(f"<html><h1>www.cskaoyan.com</h2></html>不是符合要求的标签！")


def number_generator(start=0):
    """
    使用yield创建一个生成器；生成器是迭代器的子类
    函数中出现 yield 关键字，调用函数不会执行函数体，而是返回生成器对象。
    :param start:
    :return:
    """
    while True:  # 无限循环，持续生成数字
        yield start  # 程序在这里暂停，并return start的值
        start += 1  # 下次继续执行


def use_generator():
    """
    练习使用生成器
    :return:
    """
    gen = number_generator()  # 创建生成器实例，从0开始；gen接收一个生成器
    print(next(gen))  # 输出0 拿到start的值，并next迭代到下一个
    print(next(gen))  # 输出1
    print(next(gen))  # 输出2

    gen2 = number_generator(10)
    print(next(gen2))  # 输出10
    print(next(gen2))  # 输出11


def number_generator1(start=0):
    while start <= 5:
        yield start
        start += 1


def use_generator1():
    """
    使用生成器例二
    :return:
    """
    gen = number_generator1()
    for i in gen:
        print(i)  # 输出0到5


def find_second_match(pattern, text):
    """
    利用finditer获取第二个匹配项
    :param pattern:
    :param text:
    :return:
    """
    matches = re.finditer(pattern, text)  # 迭代器
    try:
        # next会先返回迭代器，然后直接跳到下一个
        next(matches)  # 获取第一个匹配项，直接跳过、不接收
        second_match = next(matches)  # 获取接收第二个匹配项
        return second_match.group()
    except StopIteration:
        return "后面没有了"


def add(x):
    result = x.group()
    return str(int(result) + 100)


def use_advance():
    """
    re高级用法
    :return:
    """
    # search只能搜索第一个
    if ret := re.search(r"\d+", "阅读次数为 9999,点赞888"):
        print(ret.group())
    print("-" * 100)

    # 练习re.finditer
    text = "abc123def456ghi789"
    pattern = r"\d+"
    second_match = find_second_match(pattern, text)
    print(second_match)
    print("-" * 100)

    # findall 返回匹配的所有项的列表
    # 需求：统计出 python、c、c++相应文章阅读的次数
    if ret := re.findall(r"\d+", "python = 9999,c = 7890,c++ = 12345"):
        print(ret)  # ['9999', '7890', '12345']
    print("-" * 100)

    # sub 将匹配到的数据进行替换
    ret = re.sub(r"\d+", "998", "python = 997")
    print(ret)  # python = 998
    print("-" * 100)

    # sub配合lambda表达式
    ret = re.sub(r"\d+", lambda x: str(int(x.group()) + 100), "python = 997")
    print(ret)  # python = 1097
    print("-" * 100)

    # sub配合自定义函数
    ret = re.sub(r"\d+", add, "python = 997")
    print(ret)  # python = 1097
    print("-" * 100)

    # sub 设置替换次数
    text = "apple apple apple apple"
    pattern = r"apple"
    replacement = "orange"
    new_text = re.sub(pattern, replacement, text, count=2)
    print(new_text)


def use_findall():
    """
    findall的问题
    :return:
    """
    s = "hello world, now is 2020/7/20 18:48, 现在是 2020年7月20日18时48分。"
    ret_s = re.sub(r"[年月]", r"/", s)
    ret_s = re.sub(r"日", r" ", ret_s)
    ret_s = re.sub(r"[时分]", r":", ret_s)
    print(f"ret_s: {ret_s}")

    # findall存在的问题:不加?: 会只匹配分组的内容
    pattern = re.compile(
        r"\d{4}/[01]?[0-9]/[1-3]?[0-9]\s(0[0-9]|1[0-9]|2[0-4]):[0-5][0-9]"
    )
    ret = pattern.findall(ret_s)
    print(ret)  # ['18', '18'] 只匹配提取了分组的内容
    print(f"修改后：")
    pattern = re.compile(
        r"\d{4}/[01]?[0-9]/[1-3]?[0-9]\s(?:0[0-9]|1[0-9]|2[0-4]):[0-5][0-9]"
    )
    ret = pattern.findall(ret_s)
    print(ret)  # ['2020/7/20 18:48', '2020/7/20 18:48'] 想要的结果

    # search 没问题
    if ret1 := re.search(pattern, ret_s):
        print(ret1.group())


def use_sub_split():
    """
    练习sub和split
    :return:
    """
    # 用三引号定义长文本
    long_text = """
    abc'def"hahah
    """
    print(long_text)
    print("-" * 100)

    # 需求：从下面的字符串中取出文本，去掉各种标签
    long_text = """
    <div>
<p>岗位职责：</p>
<p>完成推荐算法、数据统计、接口、后台等服务器端相关工作</p>
<p><br></p>
<p>必备要求：</p>
<p>良好的自我驱动力和职业素养，工作积极主动、结果导向</p>
<p>&nbsp;<br></p>
<p>技术要求：</p>
<p>1、一年以上 Python 开发经验，掌握面向对象分析和设计，了解设计模式</p>
<p>2、掌握 HTTP 协议，熟悉 MVC、MVVM 等概念以及相关 WEB 开发框架</p>
<p>3、掌握关系数据库开发设计，掌握 SQL，熟练使用 MySQL/PostgreSQL 中的一种<
br></p>
<p>4、掌握 NoSQL、MQ，熟练使用对应技术解决方案</p>
<p>5、熟悉 Javascript/CSS/HTML5，JQuery、React、Vue.js</p>
<p>&nbsp;<br></p>
<p>加分项：</p>
<p>大数据，数理统计，机器学习，sklearn，高性能，大并发。</p>
</div>
    """
    print(long_text)
    # 当 ^ 出现在 [] 第一个字符时，含义不再是以什么字符开头：而代表不匹配括号内任意字符。
    # 将 任何非>的字符 &nbsp;即空格 \n 全部替换为空
    if ret := re.sub(r"<[^>]*>|&nbsp;|\n|\s", "", long_text):
        print(ret)
    print("-" * 100)

    # 需求：切割字符串"info:xiaoZhang 33 shandong"
    ret = re.split("[: ]", "info:xiaoZhang 33 shandong")
    print(ret)  # ['info', 'xiaoZhang', '33', 'shandong']


if __name__ == "__main__":
    # use_simple()
    # use_single()
    # use_multiple()
    # start_end()
    # split_group()
    # use_advance()
    # use_findall()
    use_sub_split()

    # use_generator()
    # <generator object number_generator at 0x000001DB11956140> function加了yield之后变成generator
    # print(number_generator())
    # use_generator1()
