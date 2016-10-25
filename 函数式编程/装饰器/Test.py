# coding=utf-8
import functools


# 1. 请编写一个decorator，能在函数调用的前后打印出'begin call'和'end call'的日志。
def decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print("begin call")
        func(*args, **kw)
        print("end call")

    return wrapper


@decorator
def former_func():
    print("I am former func")


former_func()
print()


# 2
# 再思考一下能否写出一个@log的decorator，使它既支持：
#
# @log
# def f():
#     pass
# 又支持：
#
# @log('execute')
# def f():
#     pass

def log(*log_args):
    def decorator_inside(func):
        str_begin = ""
        if len(log_args) == 0:
            str_begin = "begin call"
        else:
            str_begin = log_args[0] + "begin call"

        def wrapper(*args, **kw):
            print(str_begin)
            func(*args, **kw)
            print("end call")

        return wrapper

    return decorator_inside


@log()
def former_log_func():
    print("this is the log func")


former_log_func()
