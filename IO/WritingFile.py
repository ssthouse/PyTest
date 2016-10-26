# coding=utf-8

# 1.write file
f = open("test.txt", "w")
f.write("I write in the file!")
f.close()


# 2.use with to write file
with open("test.txt", "w") as f:
    f.write("I write file with 'with' !")
