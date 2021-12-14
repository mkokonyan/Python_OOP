def fibonacci():
    first_num = 0
    yield first_num
    second_num = 1
    yield second_num
    previous_num = first_num
    current_num = second_num
    while True:
        yield current_num + previous_num
        temp = previous_num
        previous_num = current_num
        current_num = current_num + temp



generator = fibonacci()
for i in range(12):
    print(next(generator))
