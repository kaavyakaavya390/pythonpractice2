def generator(val):
    print("val+2")
    yield val + 2
    print("val*2")
    yield val * 2
    print("val/2")
    yield val / 2
    print("val-2")
    yield val - 2




for val in generator(4):
    print(val)
names = ["Abi", "Bhavani", "Sham", "Santhiya"]
genobj = (x * 4 for x in generator(8))
print(genobj)
for i in genobj:
    print(i)
# it.send("name")