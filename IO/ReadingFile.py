# coding=utf-8

# 1.try open and read a file
f = open("test.txt", "r")
print(f.read())
f.close()
print()

# 2.use 'try' to release the resouce
try:
    f = open("test.txt", "r")
    print(f.read())
    print()
finally:
    if f:
        f.close()

# 3.use 'with' to simplify te code, no need to write f.close()
with open("test.txt", "r") as f:
    print(f.read())
