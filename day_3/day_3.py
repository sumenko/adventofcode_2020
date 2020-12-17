"""
    Day #03
    https://adventofcode.com/2020/day/3
"""

courses = ((1,1), (3,1), (5,1), (7,1),(1,2)) #336

mul = 1
with open("input.txt", "r") as inp:
    lines = inp.readlines()
    for course in courses:
        X = 0
        line_number = 0
        trees = 0    
        for line in lines:
            if line_number % (course[1]) == 0:
                length = len(line)-1
                pos = X - (X // length) * length
                char = line[pos]
                if char == "#":
                    trees += 1
                X += course[0]
            line_number += 1
        mul *= trees
    print("Multiply answer:", mul)
