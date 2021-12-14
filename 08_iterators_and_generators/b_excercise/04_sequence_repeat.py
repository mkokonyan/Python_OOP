class sequence_repeat:
    def __init__(self, sequence, number):
        self.sequence = sequence
        self.idx_counter = 0
        self.end = number

    def __iter__(self):
        return self

    def __next__(self):
        if self.end == 0:
            raise StopIteration
        index = self.idx_counter
        self.idx_counter += 1
        if self.idx_counter == len(self.sequence):
            self.idx_counter = 0
        self.end -= 1
        return self.sequence[index]


result = sequence_repeat('abc', 5)
for item in result:
    print(item, end='')
