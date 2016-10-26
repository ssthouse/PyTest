# coding=utf-8
from io import StringIO

# 1.try using stringio
f = StringIO()
f.write("hello")
f.write(" ")
f.write("world")
print(f.getvalue())
print()

# 2.try read StringIO
f_read = StringIO("Hi\nthis is Mick\ngoodbye")
while True:
    s = f_read.readline()
    if s == '':
        break
    print(s.strip())
