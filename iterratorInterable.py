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

    def __contains__(self, val):
        for item in self:
            if item == val:
                return True
        return False

    def __next__(self):
        print("next called")
        if self.pointer >= len(self.col):
            self.pointer = 0
            raise StopIteration
        val = self.col[self.pointer]
        self.pointer += 1
        return val


obj = Iterator([1, 2, 3, 4, 5, 6])
for i in obj:
    for j in obj:
        print(i, j)
