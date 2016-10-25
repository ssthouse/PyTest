# coding=utf-8
import functools


# 打印属性
def fun():
    print("2016.10.24")


print(fun.__name__)
print()


# 1.单层组装饰器: 添加一个简单的打印方法名称功能
def log(func):
    # 在decorator层中进行wrap
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("call method: %s" % func.__name__)
        return func(*args, **kwargs)

    return wrapper


@log  # 这里会自动把修饰的方法作为参数传递进去
def wrapper_func():
    print("2016.10.24")


wrapper_func()
print(wrapper_func.__name__)
print()


# 2.使用三层嵌套, 可以传入参数
def log_twice(text):
    def decorator(func):
        # 在decorator中进行wrap
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print("text:%s name:%s" % (text, func.__name__))
            return func(*args, **kw)

        return wrapper

    return decorator


@log_twice("hahaha")  # 这里会自动把修饰的方法作为参数传递进去
def wrapper_func_twice():
    print("2016.10.24")


wrapper_func_twice()
print(wrapper_func_twice.__name__)
