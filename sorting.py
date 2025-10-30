li = [2, 5, "3", 3.4, True, "Apple", "orange", 5.67, False]
li = sorted(li)

print(li)

print("================================")

list2 = ["appale", "cat", "dorm", "estancia", "forum", "bigboss"]
list2.sort(key=lambda d: d[-1])
print(list2)
list2.sort(key=len)
print(list2)

print("===============================")

from functools import total_ordering


@total_ordering
class mylist:
    def __init__(self, data):
        self.data = data

    # def __lt__(self,other):
    #     print("lt..........")
    #     if(self.data<other.data):
    #         return True
    # return False
    def __gt__(self, other):
        print("gt..............")
        if self.data > other.data:
            return True
        return False

    def __ge__(self, other):
        print("gee..............")
        if self.data >= other.data:
            return True
        return False

    def __le__(self, other):
        print("le..............")
        if self.data <= other.data:
            return True
        return False

    def __ne__(self, other):
        print("ne.............")
        if self.data != other.data:
            return True
        return False

    def __eq__(self, other):
        print("eq.................")
        if self.data == other.data:
            return True
        return False

    def __repr__(self):
        return f"{self.data}"


list1 = [(mylist(3), mylist(1)), (mylist(9), mylist(5)), (mylist(1), mylist(4))]
list1 = sorted(list1,key=lambda k : k[0])
print(list1)
