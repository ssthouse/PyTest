# coding=utf-8


# 1.尝试使用@property

class Student(object):
    def __init__(self):
        self._score = 0

    @property
    def score(self):
        return self._score

    # 这一步调用的 这个修饰器  其实就是上面那个property生成的
    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError("value not supported")
        if value < 0 or value > 100:
            raise ValueError("value out of range")
        self._score = value


stu = Student()
stu.score = 99
print(stu.score)
