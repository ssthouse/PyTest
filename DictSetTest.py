# coding=utf-8

# dict test
d = {"key1": "value1", "key2": "value2", "key3": "value3"}
# 通过下标获取
print(d["key1"])
# 通过get方法获取
print(d.get("key1"))
print

# 下标设置value
d["key1"] = "I am new value1"
print(d["key1"])
print()
# test pop
print("before:")
print(d)
d.pop("key1")
print("after")
print(d)
print()
# test key in dict 方法
isKey1In = "key1" in d
isKey2In = "key2" in d
print("d contains key1: ", isKey1In)
print("d contains key2: ", isKey2In)
print()
# ***************** test set *************************
test_set = set(["item1", "item2", "item3"])
print(test_set)
# test add
test_set.add("item4")
print(test_set)
# test key in set
isItem1InSet = "item1" in test_set
print("item1 is in test_set: ", isItem1InSet)
