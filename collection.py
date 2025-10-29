from collections import Counter, OrderedDict, defaultdict, deque, namedtuple
from typing import Any

# ------------------deques--------
dq = deque([1, 2, 3])
dq.append(4)
dq.appendleft(0)
print(dq)
dq.pop()
dq.popleft()
print(dq)

# ------namedtuple-----
Point = namedtuple("point", ["x", "y"])
p = Point(10, 20)
print(type(Point))
print(p.x, p.y)
print(*p)
print(p._asdict())
# ---------deafult dict--------
d = defaultdict(int)
d["a"] += 1
d["b"] += 2
print(d)
print(d["c"])
d2 = defaultdict(list)
d2["fruits"].append("apple")
print(d2)

# -----counter----
data = ["apple", "banana", "apple", "orange", "banana", "apple"]
count = Counter(data)
count2 = Counter(data + data)
print(count)
print(list(count.elements()))
count.update(
    [
        "apple",
        "banana",
        "apple",
        "orange",
        "banana",
        "apple",
        "apple",
        "banana",
        "apple",
    ]
)
print(count.most_common(1))
print(count - count2)
print(count + count2)

# ---ordered dict----
od = OrderedDict()
od["a"] = 1
od["b"] = 2
od["c"] = 3
print(od)
del od["b"]
od["b"] = 4
print(od)
