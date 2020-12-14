# часть 2, найти 3 таких как в 1 части
from itertools import combinations
import timeit
import time

def find_two_numbers(numbers:tuple, N:int):
    """
        Часть 1
        https://adventofcode.com/2020/day/1
        найти в списке 2 числа сумма которых 2020
        вернуть их произведение
    """
    numbers2 = [N-a for a in numbers]
    for n in numbers:
        if n in numbers2:
            return n, N-n
    return None, None

def get_mima(numbers):
    return numbers[0], numbers[-1]

def get_mimima(numbers):
    return numbers[0], numbers[1] ,numbers[-1]

def print_numbers(numbers):
    print(len(numbers), ":", " ".join((str(i) for i in numbers)))

def filter_numbers(numbers:tuple, N:int):
    """ Drops numbers that we don't need"""
    numbers = sorted(numbers)
    
    mima = get_mima(numbers)
    iter = 0
    # first+last > 2020 - drop last
    while sum(mima) >= N:
        iter += 1
        
        numbers.pop(numbers.index(mima[1]))
        mima = get_mima(numbers)
        
    mimima = get_mimima(numbers)
    
    # first + second + last > 2020 - drop last
    while sum(mimima) > N:
        
        numbers.pop(numbers.index(mimima[-1]))
        mimima = get_mimima(numbers)
    
    return numbers

def find_three_dumb(numbers, N):
    combi = combinations(numbers_list, 3)
    for c in combi:
        if sum(c) == 2020:
            return c

def mul(numbers):
    m = 1
    for a in numbers:
        m*=a
    return m

with open("input.txt", "r") as fin:
    numbers_list=()
    for line in fin:
        numbers_list+=(int(line),)
    a, b = find_two_numbers(numbers_list, 2020)
    # day 1/part 1
    # print("multiply {}+{}={}: mul={} ".format(a, b, a+b, a*b))
    
    # day 1/part 2
    # faster!
    numbers_list = filter_numbers(numbers_list, 2020) 
    t0 = time.time()             
    answer = find_three_dumb(numbers_list, 2020)
    t1 = time.time()
    print("{:.2}".format(t1-t0))
    print(answer, mul(answer))