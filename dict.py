from collections import UserDict

# *************dictionary*******
print("--------creation-------")
dict1 = {}
dict2 = dict()
data = [("pen", 2), ("Pencil", 5), ("Paper", 50)]
for key, value in data:
    dict1[key] = value
k = ("Apple", "banana", "guava", "cherry")
v = (200, 300, 400, 500)
dict2[k] = v
dict3 = {conatin: count * 4 for conatin, count in dict1.items()}
dict4 = {
    "dict1": dict1,
    "dict2": dict2,
    "dict3": dict3,
    "list1": k,
    "list(tuple)": data,
    "tuple": data[0],
}
print(f"{dict1}\n{dict2}\n{dict3}\n{dict4}")

print("-----unpacking------")


def unpack(**argw):
    print(len(argw))
    return argw


dict5 = unpack(
    ten=10, eleven=11, twenty=20, **{"twenty two": 22}, var1=45, var2=55
)  # keywords must be string
print(dict5)

dict6 = dict1 | dict2
print("dict6 : ", dict6)

# -----get and setDefault------
dict6["new"] = 100
val = dict6.get("old", 200)
# print(dict6["old"])
dict6.setdefault("old", 200)
print(dict6["old"])


# ------user defined dict---------
class mydict(UserDict):
    def __missing__(self, key):
        return f"the key {key} is not there and the dictionary is {self}"


di = mydict()
di["val"] = 3
print(di["dif"])
