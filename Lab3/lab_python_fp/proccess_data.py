import json
from time import sleep
from cm_timer import cm_timer_1
from field import field
from unique import Unique
from print_result import print_result
from gen_random import gen_random


@print_result
def f1(data):
    return sorted(Unique(field(data, 'job-name'), ignore_case=True))


@print_result
def f2(data):
    return list(filter(lambda val: 'программист' in val[:11], data))


@print_result
def f3(data):
    return list(map(lambda val: val + " с опытом Python", data))


@print_result
def f4(data):
    return list(zip(data, list(map(lambda val: "Зарплата " + val + " руб", map(str, (gen_random(len(data), 10000, 20000)))))))


def main():
    with open('data_light.json', 'r', encoding='utf8') as temp:
        data = json.load(temp)
    with cm_timer_1():
        sleep(1.57)
        f4(f3(f2(f1(data))))
