def generator(val):
    print("val+2")
    yield val + 2
    print("val*2")
    yield val * 2
    print("val/2")
    yield val / 2
    print("val-2")
    yield val - 2


def coroutine():
    print("It starts.......")
    while True:
        try:
            name = yield
            print(name)
        except GeneratorExit:
            print("coroutine closed.....")
            break


for val in generator(4):
    print(val)
names = ["Abi", "Bhavani", "Sham", "Santhiya"]
obj = coroutine()
next(obj)
obj.send("Abi")
obj.close()
genobj = (x * 4 for x in generator(8))
print(genobj)
for i in genobj:
    print(i)
# it.send("name")
