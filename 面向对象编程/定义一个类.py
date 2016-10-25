# coding=utf-8

from types import MethodType


# 1.定义一个类
class Student(object):
    def __init__(self):
        self.name = "Jack"
        self.age = 11


stu = Student()
print(stu.name)
print(stu.age)
print()


# 2.给实例绑定方法
def set_age(self, age):
    self.age = age


stu.set_age = MethodType(set_age, stu)
stu.set_age(1000)
print(stu.age)
print()


# 3.给class绑定方法, 直接设置
def set_score(self, score):
    self.score = score


Student.set_score = set_score
stu_two = Student()
stu_two.set_score(100)
print(stu_two.score)


# 4.限定所有可以绑定的属性(注意, 这个slots只对当前定义的类起作用)
class Class(object):
    __slots__ = ("name", "number")


class_one = Class()
class_one.name = "ClassOne"
class_one.number = 54
# class_one.size = 100
