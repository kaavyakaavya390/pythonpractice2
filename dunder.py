class MyClass:
    clsdata = [1, 2, 3, 4, 5, 6]

    def __init__(self, data):
        self.data = data

    def __getitem__(self, index):
        return self.data[index]

    def __class_getitem__(self, index):
        return self.clsdata[index]

    def __delitem__(self, val):
        if val in self.data:
            self.data.remove(val)
        else:
            raise ValueError


class Multiple:
    def __init__(self, lists):
        self.lists = lists

    def __getitem__(self, index):
        if isinstance(index, tuple):
            list_ind = index[0]
            ele_ind = index[1]
            # print(type(ele_ind))
            return self.lists[list_ind][ele_ind]
        else:
            return self.lists[index]

    def __setitem__(self, index, val):
        if isinstance(index, tuple):
            list_ind = index[0]
            ele_ind = index[1]
            self.lists[list_ind][ele_ind] = val
        else:
            self.lists[index] = val

    def __str__(self):
        return f"Multiple : {self.lists}"


class Dict:
    def __init__(self, collect):
        self.collect = collect

    def __getitem__(self, key):
        if key in self.collect:
            return self.collect[key]
        else:
            return f"Error : key {key} not found"

    def __repr__(self):
        return f"Dict({self.collect})"

    def __str__(self):
        return f"{self.collect}"

    def __delitem__(self, key):
        if key in self.collect:
            del self.collect[key]
        else:
            raise KeyError


obj = MyClass([23, 45, 20, 56])
del obj[23]
print(obj[0])
print(dir(obj))
multi = Multiple([[1, 2, 3, 4, 5], ["a", "b", "c", "d"]])
print(multi[0])
print(multi[1])
print(multi[0, 4])
multi[0] = multi[0, 2:5]
print(multi)

dict_handle = Dict({"apple": 40, "orange": {"kg": 45, "gram": 26}, "pineapple": 45})
print(repr(dict_handle))
print(str(dict_handle))
print(dict_handle["apple"])
print(dict_handle)
obj2 = eval(repr(dict_handle))
del obj2["apple"]
print(repr(obj2))
