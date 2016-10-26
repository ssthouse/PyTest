# coding=utf-8
import base64
str_encode = base64.b64encode(b'binary\x00string')
print(str_encode)
str_decode = base64.b64decode(str_encode)
print(str_decode)

