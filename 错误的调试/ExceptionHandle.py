# coding=utf-8

# 1.try using try catch grammer
try:
    print("using try")
    a = 10 / 0
except ZeroDivisionError as e:
    print("exception: %s" % e)
finally:
    print("finally")
print("hahaha go on running")
print()

# 2. try another exception type
try:
    print("using try")
    a = 10 / int('a')
except ValueError as e:
    print("exception: %s" % e)
except ZeroDivisionError as e:
    print("exception: %s" % e)
finally:
    print("finally")
print("two error test, still running")
print()

# 3.try else usage
try:
    print("using try")
except ValueError as e:
    print("exception: %s" % e)
else:
    print("no exception occur")
finally:
    print("finally")
print("try else still running")

