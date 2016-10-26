# coding=utf-8
from collections import namedtuple
from collections import deque
from collections import defaultdict
from collections import OrderedDict
from collections import Counter

# 1.using namedtuple
Point = namedtuple("Point", ["x", "y"])
p = Point(10, 20)
print(p.x)
print(p.y)
print(type(p))
print()

# 2.using deque: double ended queue
# special func: popleft appendleft
double_ended_queue = deque(["a", "b", "c"])
double_ended_queue.append("d")
double_ended_queue.appendleft("0")
print(double_ended_queue)
print(type(double_ended_queue))
print()

# 3.using default dic
# speciality: return specific things when key doesn't exit
dd = defaultdict(lambda: "N/A")
dd["key1"] = "abc"
print(dd["key1"])
print(dd["key2"])
print()

# 4.using ordered dict
# speciality: the key stores in the order when it was inserted
former_dic = dict(a=1, b=2, c=3)
print(former_dic)
order_dic = OrderedDict()
order_dic["b"] = 2
order_dic["a"] = 1
order_dic["c"] = 3
print(order_dic)
print()

# 5.using counter
# speciality: the default of this dict is zero
c = Counter()
for ch in "Programming":
    c[ch] += 1
print(c)
print()