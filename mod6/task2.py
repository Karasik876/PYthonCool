class DoubleElement:
    def __init__(self, *lst):
        self.data = lst
        self.index = 0

    def __next__(self):
        if self.index < len(self.data) - 1:
            pair = (self.data[self.index], self.data[self.index + 1])
            self.index += 2
            return pair
        elif self.index == len(self.data) - 1:
            pair = (self.data[self.index], None)
            self.index += 2
            return pair
        else:
            raise StopIteration

    def __iter__(self):
        return self

dL = DoubleElement(1, 2, 3, 4)
for pair in dL:
    print(pair)

print()

dL = DoubleElement(1, 2, 3, 4, 5)
for pair in dL:
    print(pair)