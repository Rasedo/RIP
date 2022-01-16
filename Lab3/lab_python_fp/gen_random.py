from random import randint


def gen_random(num_count, begin, end):
    for i in range(0, num_count):
        yield randint(begin, end)


for val in gen_random(5, 1, 3):
    print(val)
