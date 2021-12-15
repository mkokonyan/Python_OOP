class countdown_iterator:
    def __init__(self, end):
        self.end = end
        self.start = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.end < 0:
            raise StopIteration
        value = self.end
        self.end -= 1
        return value


iterator = countdown_iterator(10)
for item in iterator:
    print(item, end=" ")
