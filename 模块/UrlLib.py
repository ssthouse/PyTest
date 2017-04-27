# coding=utf-8
from urllib import request

# using get
# with request.urlopen("https://api.douban.com/v2/book/2129650") as f:
#     data = f.read()
#     print("Status: ", f.status, f.reason)
#     print()
#     for k, v in f.getheaders():
#         print("%s     %s" % (k, v))
#     print()
#     print("Data: ", data.decode("utf-8"))
#     print()

# buiding Request to imitate the browser
req = request.Request("http://www.douban.com/")
req.add_header(
    "User-Agent",
    "Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25")
with request.urlopen(request) as f:
    print("Status: ", f.status, f.reason)
    for k, v in f.getheaders():
        print(k, "  ", v)
