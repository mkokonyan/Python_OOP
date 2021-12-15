def get_primes(obj):
    for i in range(len(obj)):
        current_num = obj[i]
        if current_num > 1:
            if current_num == 2:
                yield current_num
            for j in range(2, current_num):
                if current_num % j == 0:
                    break
                if j == current_num - 1:
                    yield current_num

print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))
