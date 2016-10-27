# coding=utf-8
# the itertools provides powerful functions to iterate many objects
import itertools

# using iter count
nature = itertools.count()
for n in nature:
    if n < 100:
        print(n)
    else:
        break
print()

# using cycle: to repeat the sequence that
cycle_iter = itertools.cycle("ABC")
n = 0
for a in cycle_iter:
    n += 1
    if n > 100:
        break
    print(a)
print()

# using repeat
repeat_iter = itertools.repeat("abc", 10)
for a in repeat_iter:
    print(a)
print()

# using take_while to get a limited iterator
nature2end = itertools.count(1)
limited_iterator = itertools.takewhile(lambda x: x < 10, nature2end)
print(list(limited_iterator))
print()

# using chain to generate a bigger iterator
for c in itertools.chain("I am", "ssthouse"):
    print(c)
print()

# using group_by to divide the same & continuous sequence
for key, group in itertools.groupby("AAABBCCCCC"):
    print(key, "  ", list(group))
