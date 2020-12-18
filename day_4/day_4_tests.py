from day_4 import is_hcl_correct, is_pid_correct, is_hgt_correct, is_ecl_correct


# haircolor test
hcl_test = {hcl: is_hcl_correct(hcl) 
            for hcl in ("#123abc", "#123abz", "123abc")}
print("hcl: ", hcl_test)
# pid test
pid_test = {pid: is_pid_correct(pid) 
            for pid in ("000000001", "0123456789")}
print("pid: ", pid_test)
# hgt test
hgt_test = {hgt: is_hgt_correct(hgt) 
            for hgt in ("60in", "190cm", "190in", "190")}
print("hgt: ", hgt_test)

# ecl test
ecl_test = {ecl: is_ecl_correct(ecl) 
            for ecl in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth", 
            "wat", "zzz")}
print("ecl: ", ecl_test)