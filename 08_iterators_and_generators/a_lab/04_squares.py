def squares(n):
    current_num = 1
    while current_num <= n:
        yield current_num ** 2
        current_num += 1


print(list(squares(5)))

class squares_iter:
    def __init__(self, end):
        self.end = end
        self.start = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.start > self.end:
            raise StopIteration
        temp = self.start
        self.start += 1
        return temp ** 2

print(list(squares_iter(5)))


