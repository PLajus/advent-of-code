import os

here = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(here, "input.txt")
my_file = open(filename, "r")
f_contents = my_file.read().splitlines()
my_file.close()


def password_validation(*args):
    valid_pass_count = 0
    keycount = 0 # number of keys, need 7 wihout [cid] for pass to be valid
    for line in f_contents:
        if line == "": # new entry seperated by an empty line
            if keycount == len(args): # check if entry has 7 keys
                valid_pass_count += 1
            keycount = 0 # reset key count for next entry
            continue
        for field in line.split():
            key, value = field.split(':') # split field into key and value, used to count keys ignoring [cid]
            if key in args:
                keycount += 1
    return valid_pass_count

# Part 1
print(password_validation("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"))