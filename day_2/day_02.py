"""
    Day #02. Find valid passwords
    https://adventofcode.com/2020/day/2#
    https://adventofcode.com/2020/day/2#part2
"""


def parse_line(line):
    splitted = line.split(" ")
    first, second = (int(i) for i in splitted[0].split("-"))
    symbol = splitted[1].split(":")[0]
    password = splitted[2].split("\n")[0]
    return first, second, symbol, password


def is_valid_part_one(frst, scnd, symbol, password):
    # first, second, symbol, password = packed
    # line = '11-12 n: nnnnnnnnnnnn'
    return 1 if frst <= password.count(symbol) <= scnd else 0


def is_valid_part_two(frst, scnd, symbol, password):
    """ Exactly one of these positions must contain the given letter """
    return 1 if [password[frst-1], password[scnd-1]].count(symbol) == 1 else 0


with open("input.txt", "r") as inp:
    lines = [line for line in inp.readlines()]
    print("Total passwords in base:", len(lines))
    count_one = 0
    count_two = 0
    line_number = 0

    for line in lines:
        line_number += 1
        parsed = parse_line(line)
        count_one += is_valid_part_one(*parsed)
        count_two += is_valid_part_two(*parsed)

    print("Valid passwords (part one):", count_one)
    print("Valid passwords (part two):", count_two)
