from time import sleep, time
from contextlib import contextmanager


class cm_timer_1:
    def __init__(self):
        self.timer = time()

    def __enter__(self):
        pass

    def __exit__(self, exp_type, exp_value, traceback):
        self.timer = time() - self.timer
        print(self.timer)


@contextmanager
def cm_timer_2():
    timer = time()
    yield
    timer = time() - timer
    print(timer)


with cm_timer_1():
    sleep(2)
with cm_timer_2():
    sleep(3)

