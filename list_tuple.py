from array import array

import numpy as np

# -*-*-*-*-*-*-*-*-*-*-*-*-*-List creations-*-*-*-*-*-*-*-*-*-*-*-*-*-
list1 = []
twod = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]]

list2 = list()
for i in range(1, 10):
    list1.append(i)
# -*-*-*-*-*-*-List comprehention-*-*-*-*-*-*-*-
list3 = [x for x in range(10) if x % 2 == 0]
# -*-*-*-*-*-*-List geerater expression-*-*-*-*-*-*-*-
list4 = list(((2, y) for y in range(10) if y % 2 == 0))
list5 = list(filter(lambda c: c[1] > 2, list4))
# -*-*-*-*-*-*- Access elements in list *-*-*-*-*-*-*-
print("by index (list1[0]): ", list1[0])
print("whole list2 : ", list2)
print("count : ", list3.count(2))
print(list5)

print(twod[0][1:3])
# -*-*-*-*-*-*-*-*-*-*-*-*-*- Tuple -*-*-*-*-*-*-*-*-*-*-*-*-*
tup = tuple()
tup2 = ()
tup3 = (1,)
tup4 = (3, 2, 5, 1)
tup = tuple((str(x) for x in range(50, 60)))
print(type(tup3))
# -*-*-*-*-*-*- Tuple operation-*-*-*-*-*-*
tup5 = tup + tup3
print(tup5)
print("Union : ", tup4 or tup3)
print("Intersection : ", tup5 and tup3)

# -*-*-*-*-*-*-unpacking-*-*-*-*-*-*-
birthday = [5, 5, 2005]
date, day, year = birthday
print(f"date {date} day {day} year {year}")


def func():
    for i in range(1, 4):
        yield i


a, b, c = func()
print(f"{a} {b } {c}")
# using *
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
a, b, *balance = arr
print(f"{a} {b} {balance}")
print(*range(10), "The end")
list1 = list(range(2, 11))
print(list1)

# nested unpacking
nested = [
    (2, 4, ("name1", "name2")),
    (4, 2, ("name3", "name4")),
    (1, 6, ("name5", "name6")),
    (1, 1, ("name7", "name8")),
    (9, 0, ("name9", "name10")),
]
for first, _, (name, subname) in nested:
    print(f"{first} | {name} | {subname}")


# -*-*-*-*-*-*-ARRAY-*-*-*-*-*-*-
array1 = array("i", (x for x in range(10)))
print(array1[9])

# -*-*-*-*-*-*-meory view-*-*-*-*-*-*-
li = array("B", [10, 20, 30, 40, 50, 60])
mv1 = memoryview(li)
sli = mv1[3:6]
print(f"{mv1}  list-> {mv1.tolist()}")
print(sli)
print(sli.tolist())
mv2 = mv1.cast("B", [6, 1])
print(mv2.tolist())

# numpy
data = np.arange(10)
print(data)
print(data[:, 4])
