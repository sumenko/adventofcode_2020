def parse_line(line):
    splitted = line.split(" ")
    first, second = (int(i) for i in splitted[0].split("-"))
    symbol = splitted[1].split(":")[0]
    password = splitted[2]
    return first, second, symbol, password

def is_valid_part_one(packed):
    first, second, symbol, password = packed
    # line = '11-12 n: nnnnnnnnnnnn'    
    return 1 if first <= password.count(symbol) <= second else 0

def is_valid_part_two(packed):
    pass

with open("input.txt", "r") as inp:
    lines = [line for line in inp.readlines()]
    print("Passwords in base:", len(lines))
    count = 0
    for line in lines:
        count+=is_valid_part_one(parse_line(line))
    print("Valid passwords (part one):", count)
