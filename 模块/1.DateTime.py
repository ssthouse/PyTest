# coding=utf-8 try using datetime
from datetime import datetime

# 1.get current time
now = datetime.now()
print(now)
print(type(now))
print()

# 2.use constructor to build datetime
dt = datetime(2016, 10, 26, 7, 30)
print(dt)
print()

# 3.get timestamp
print(now.timestamp())
print()

# 4.transfer timestamp to datetime
now_date = datetime.fromtimestamp(dt.timestamp())
print(now_date)
print()

# 5.convert str to datetime
# notice that the datetime which is got in this way doesn't have the timezon
str_time = "2016-10-26 19:39:00"
str_format = "%Y-%m-%d %H:%M:%S"
date_from_str = datetime.strptime(str_time, str_format)
print(date_from_str)
print()

# 6.get the format str from datetime
