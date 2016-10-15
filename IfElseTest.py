# coding=utf-8
# 测试if else 判断
from pip._vendor.distlib.compat import raw_input

strNum = raw_input("input weight:\t")

intNum = int(strNum)

if intNum >= 80:
    print("heavy")
elif intNum >= 70:
    print("ok")
else:
    print("thin")
