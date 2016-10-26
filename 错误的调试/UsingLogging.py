# coding=utf-8
import logging

# 1.try using logging
try:
    print("using try")
    a = 10 / 0
except ZeroDivisionError as e:
    logging.exception(e)
finally:
    print("finally")
print("go on running")
