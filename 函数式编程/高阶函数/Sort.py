# coding=utf-8

# 其实这个Java也有啊, 一个静态方法, 传进来一个数组, 一个比较的接口Comparable<>
# 好吧, 和java的不太一样, 这个是对于每一个数据进行了一次映射, 映射为新的数据进行比较

# python自带方法: sorted() 传入一个参数的时候直接默认比较   传入两个参数的时候, 后一个是比较的函数

num_list = [36, 5, -12, 9, -21]
new_list = sorted(num_list)

print(new_list)
print()
print(num_list)
print()

# 传入第二个参数
sort_list = sorted(num_list, key=abs)
print(sort_list)
print()

str_list = ['bob', 'about', 'Zoo', 'Credit']
str_list_sorted = sorted(str_list, key=str.lower)
print(str_list_sorted)
print()

# 逆序输出, 其实这里要比java麻烦一点了哦, 抽象的不是比较的逻辑, 而是映射的逻辑, 还是有问题的
str_list_reverse = sorted(str_list, key=str.lower, reverse=True)
print(str_list_reverse)
print()

# 练习题
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]


# sort by name
def sort_by_name(bean):
    return bean[0]


bean_list_sorted = sorted(L, key=sort_by_name)
print(bean_list_sorted)
print()


# sort by score
def sort_by_score(bean):
    return bean[1]


bean_list_sorted_by_score = sorted(L, key=sort_by_score)
print(bean_list_sorted_by_score)
