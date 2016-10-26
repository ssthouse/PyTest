# coding=utf-8
import re

str_test = "100-12345"
str_re = r"^\d{3}\-\d{3,8}$"
if re.match(str_re, str_test):
    print("matches")
else:
    print("fail")
