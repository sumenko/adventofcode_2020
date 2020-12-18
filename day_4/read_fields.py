"""
    Read fields to check from file like
    byr (Birth Year)
    iyr (Issue Year)
    eyr (Expiration Year)
    hgt (Height)
    hcl (Hair Color)
    ecl (Eye Color)
    pid (Passport ID)
    cid (Country ID)   
"""

def read_fields(fname="fields.txt"):
    """ read fields to check """
    #    byr (Birth Year)
    fields = ()
    with open(fname, "r") as inp:
        for line in inp.readlines():
            fields += (line.strip().split("(")[0].strip(),)
    return fields


if __name__ == "__main__":
    print(read_fields())