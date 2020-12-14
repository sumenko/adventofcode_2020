"""
    Day #03
    https://adventofcode.com/2020/day/3
"""

# course = (3,1)
courses = ((1,1), (3,1), (5,1), (7,1),(1,2)) #336
# courses = ((3,1),(3,1),(3,1),)
s_open = "."
s_tree = "#"
mul = 1
with open("input.txt", "r") as inp:
    lines = inp.readlines()
    for course in courses:
        X = 0
        line_number = 0
        trees = 0    
        for line in lines:
            line_number += 1
            if line_number % course[1] + 1:
                length = len(line)-1
                pos = X - (X // length) * length
                char = line[pos]
                if char == s_tree:
                    trees += 1
                X += course[0]
        mul *= trees
        print(f"Trees encounter: {trees}")
    print("Multiply answer:", mul)