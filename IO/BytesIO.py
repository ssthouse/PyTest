# coding=utf-8
from io import BytesIO

# 1.build bytesIO
s = BytesIO()
s.write("中国".encode("utf-8"))
print(s.getvalue())
print()

# 2.read bytesIO
f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
print(f.read())