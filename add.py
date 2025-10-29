class MyClass:
    def __init__(self, data):
        self.data = data

    def __add__(self, other):
        return MyClass(self.data + other.data)

    def __str__(self):
        return f"{self.data}"

    # ----len---
    def __len__(self):
        return len(self.data)

    # -------eq------
    def __eq__(self, other):
        return self.data == other.data

    # ----call----
    def __call__(self, val):
        self.data.append(val)
        print("added val ", val)
        return self.__str__()


list1 = MyClass([1, 2, 3, 4, 5])
list2 = MyClass([6, 7, 8, 9, 10])
list3 = list1 + list2
print("list1 : ", list1)
print("list2 : ", list2)
print(list3)
print("Length of my object : ", len(list3))
print(list1 == list2)
print(list1(10))
