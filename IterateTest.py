# coding=utf-8

# for 循环
temp_list = [1, 2, 3, 4, 5]
temp_sum = 0
for num in temp_list:
    temp_sum += num
print("sum =", temp_sum)
print("")

# try range: 直接生成的就是list
temp_range = range(10)
temp_range.append(10)
for temp_num in temp_range:
    print(temp_num)
print("")

# try while
n = 10
while n > 0:
    n -= 1
    print(n)
