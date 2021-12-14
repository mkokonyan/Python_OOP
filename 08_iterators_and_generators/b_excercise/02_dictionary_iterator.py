class dictionary_iter:
    def __init__(self, obj):
        self.object = obj
        self.start = 0
        self.end = len(obj) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.start > self.end:
            raise StopIteration
        index = self.start
        self.start += 1
        return list(self.object.items())[index]


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)
