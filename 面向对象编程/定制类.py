# coding=utf-8


# 1.定制__slots__
class Student(object):
    __slots__ = ("name", "age")

    def __init__(self):
        self.name = "Jack"
        self.age = 21


stu = Student()
print(stu.name)
print(stu.age)
print(stu)
print()


# 2.定制__str__
class StudentWithStr(object):
    __slots__ = ("name", "age")

    def __init__(self):
        self.name = "Jack"
        self.age = 21

    def __str__(self):
        return "Student name%s age%d" % (self.name, self.age)

stu_with_str = StudentWithStr()
print(stu_with_str.name)
print(stu_with_str.age)
print(stu_with_str)
print()
