class Iterator:
    def __init__(self, col):
        self.col = col
        self.pointer = 0

    def __getitem__(self, index):
        print("get item called....")
        return self.col[index]

    def __iter__(self):
        print("__iter__ called")
        return self

    def __next__(self):
        # print("next called")
        if self.pointer >= len(self.col):
            self.pointer = 0
            raise StopIteration
        val = self.col[self.pointer]
        self.pointer += 1
        return val


class Mydict:
    def __init__(self, dd):
        self.dd = dd
        self.keys = list(dd.keys())
        self.pointer = 0

    def __iter__(self):
        return DcitIteratorn(self.dd)


class DcitIteratorn:
    def __init__(self, dd):
        self.dd = dd
        self.keys = list(dd.keys())
        self.pointer = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.pointer >= len(self.keys):
            raise StopIteration
        key = self.keys[self.pointer]
        self.pointer += 1
        return key


class MyList:
    def __init__(self, mylist):
        self.mylist = mylist

    def __iter__(self):
        return Iterator(self.mylist)

    def __contains__(self, val):
        print("contains called......")
        for item in range(0, len(self.mylist)):
            if self.mylist[item] == val:
                return True
        return False


# mylist=MyList(["list","tuple","dict","def","class","dunder","oops","iter"])
# for i in mylist:
#     print(i)
# for list
data = [2, 4, 1, 6, 7, 2, 0, 5, 7, 1]
mylist = MyList(data)
it = iter(mylist)
while True:
    try:
        print(next(it))
    except StopIteration:
        break
for val in it:
    print(val)

# for dictionary
items = {"a": 2, "b": 4, "c": 6, "s": 0}
for key in Mydict(items):
    print(f"{key} -> {items[key]}")
print(7 in mylist)
