def print_result(func):
    def decorated_func(*args, **kwargs):
        print(func.__name__)
        if isinstance(func(*args, **kwargs), dict):
            for key in func(*args, **kwargs):
                print(key, '=', func(*args, **kwargs)[key])
        elif isinstance(func(*args, **kwargs), list):
            for item in func(*args, **kwargs):
                print(item)
        else:
            print(func(*args, **kwargs))
        return func(*args, **kwargs)

    return decorated_func


@print_result
def test_1():
    return 1


@print_result
def test_2():
    return 'iu5'


@print_result
def test_3():
    return {'a': 1, 'b': 2}


@print_result
def test_4():
    return [1, 2]


if __name__ == '__main__':
    print('!!!!!!!!')
    test_1()
    test_2()
    test_3()
    test_4()
