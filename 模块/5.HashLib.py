# coding=utf-8
import hashlib

# 1.using md5
md5 = hashlib.md5()
str_md5 = "this is a string by ssthouse".encode("utf-8")
print(type(str_md5))
md5.update(str_md5)
print(md5.hexdigest())
print()

# 2.using sha1
sha1 = hashlib.sha1()
str_sha1 = "this is another str by ssthouse".encode("utf-8")
sha1.update(str_sha1)
print(sha1.hexdigest())
