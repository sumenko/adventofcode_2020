"""
    Day #04. Is passport valid?
    Author: Sumenko Vladimir
    https://adventofcode.com/2020/day/4
    part 01: 245
    part 02: 133
"""


def is_valid(line, fields):
    for field in fields:
        if field not in line.keys():
            return False
    return True


def is_hcl_correct(hcl):
    """ (Hair Color) - a # followed by exactly six characters 0-9 or a-f. """
    if hcl[0] == "#" and len(hcl) == 7:
        try:
            int(hcl[1:], 16)
            return True
        except ValueError:
            pass
    return False


def is_ecl_correct(ecl):
    """ (Eye Color) - exactly one of: amb blu brn gry grn hzl oth. """
    if ecl in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth"):
        return True
    return False


def is_pid_correct(pid):
    """ (Passport ID) - a nine-digit number, including leading zeroes. """
    if len(pid) == 9 and pid.isdigit():
        return True
    return False


def is_hgt_correct(hgt):
    """(Height) a number followed by either cm or in and in interval"""
    interval = {"cm": (150, 193), "in": (59, 76)}
    height = hgt.split("cm")[0].split("in")[0]  # too lo-o-o-ong
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
            if field == "byr" and 1920 <= int(line[field]) <= 2002:
                continue
            if field == "iyr" and 2010 <= int(line[field]) <= 2020:
                continue
            if field == "eyr" and 2020 <= int(line[field]) <= 2030:
                continue
            if field == "hgt" and is_hgt_correct(line[field]):
                continue
            if field == "hcl" and is_hcl_correct(line[field]):
                continue
            if field == "ecl" and is_ecl_correct(line[field]):
                continue
            if field == "pid" and is_pid_correct(line[field]):
                continue
            # nothing found - invalid
        return False
    # all done - valid
    return True


def check_batch(fname, is_valid_func, fields, batch_name=""):
    with open(fname, "r") as inp:
        valid = 0
        wait_new_line = False
        docs_collected = 0
        doc = {}

        for line in inp.readlines():
            line = line.split("\n")[0]

            if line == "":  # empty line, document is done
                doc = {}
                wait_new_line = False
                docs_collected += 1
                continue
            if wait_new_line:  # if last doc is valid
                continue

            # collect data
            doc.update(
                {k: v for k, v in (kv.split(":") for kv in line.split(" "))}
                )
            # increment if only is valid, then just wait for new line or EOF
            if is_valid_func(doc, fields) is True:
                valid += 1
                wait_new_line = True

        # last line was not empty
        if line != "":
            docs_collected += 1

        print(f"{batch_name}: {valid}/{docs_collected}")


if __name__ == "__main__":
    fields = ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid')

    fname = "input.txt"
    check_batch(fname, is_valid_data, fields, "soft check")
    check_batch(fname, is_valid, fields, "hard check")
