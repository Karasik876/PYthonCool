def armstrong():
    res = 10
    while True:
        digits = [int(x) for x in str(res)]
        nd = len(digits)
        powers_sum = sum([x ** nd for x in digits])
        if powers_sum == res:
            yield res
        res+=1

generator = armstrong()

def get_armstrong_numbers():
    return next(generator)

for i in range(8):
    print(get_armstrong_numbers(), end = ' ')