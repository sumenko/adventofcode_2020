
"""
    Day #04. Is passport valid?
    https://adventofcode.com/2020/day/4
    part 01: 245
    part 02: ?
"""


def is_valid(line, fields):
    for field in fields:
        if field not in line.keys():
            return False
    return True


def is_hcl_correct(hcl):
    """ (Hair Color) - a # followed by exactly six characters 0-9 or a-f. """
    # TODO
    if hcl[0] == "#" and len(hcl) == 7:
        try:
            int(hcl[1:], 16)
            return True
        except ValueError:
            pass
    return False


def is_ecl_correct(ecl):
    print(ecl)
    if ecl in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth"):
        return True
    return False


def is_pid_correct(pid):
    """ (Passport ID) - a nine-digit number, including leading zeroes. """
    # TODO
    if len(pid) == 9 and pid.isdigit():
        return True
    return False


def is_hgt_correct(hgt):
    """(Height) a number followed by either cm or in and in interval"""
    interval = {"cm": (150, 193), "in": (59, 76)}
    height = hgt.split("cm")[0].split("in")[0]
    units = hgt[len(height):]
    try:
        if interval[units][0] <= int(height) <= interval[units][1]:
            return True
    except KeyError:
        pass
    return False


def is_valid_data(line, fields):
    """ if one of fields incorrect - return False """
    for field in fields:
        if field in line.keys():
            # check data
            if field == "ecl":
                print(field)
            if not (
               (field == "byr" and 1920 <= int(line[field]) <= 2002) or
               (field == "iyr" and 2010 <= int(line[field]) <= 2020) or
               (field == "eyr" and 2020 <= int(line[field]) <= 2030) or
               (field == "hgt" and is_hgt_correct(line[field])) or
               (field == "hcl" and is_hcl_correct(line[field])) or
               (field == "ecl" and is_ecl_correct(line[field])) or
               (field == "pid" and is_pid_correct(line[field]))
                ):
                # print("Invalid:", field, ": ", line[field])
                return False
    # print("Valid:", field, ": ", line[field])
    return True


def read_fields(fname="fields.txt"):
    fields = ()
    with open(fname, "r") as inp:
        for line in inp.readlines():
            fields += (line.strip().split("(")[0].strip(),)
    return fields


if __name__ == "__main__":
    fields = read_fields("fields_enough.txt")
    
    with open("input.txt", "r") as inp:
        collected = []
        correct = []
        iter = 0
        doc = {}
        valid = 0
        invalid = 0
        for line in inp.readlines():
            # input(line)
            iter += 1
            line = line.split("\n")[0]

            if line == "":
                # empty line
                if is_valid(doc, fields):
                    correct.append(doc)
                    valid += 1
                else:
                    invalid += 1

                collected.append(doc)
                doc = {}
            else:
                # some data
                doc.update(
                    {k: v for k, v in (kv.split(":") for kv in line.split(" "))}
                    )
        # TODO: тут надо упростить чтобы не повторять
        if is_valid(doc, fields):
            correct.append(doc)
            collected.append(doc)
            valid += 1
            doc = {}
        status = "err"
        if valid+invalid == len(collected):
            iter = 0
            # for doc in collected:
            #     iter += 1
            #     print(f"{iter:>3}", "   ".join((f"{k}:{doc[k]:>10}" for k in sorted(doc.keys()))))
            status = "ok"
        print(f"Total/Valid: {len(collected)} / {valid} {status}")
        # print(1920 <= int('1994') <= 2002)
        