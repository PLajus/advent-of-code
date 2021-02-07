import os
import re

here = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(here, "input.txt")
with open(filename, "r") as f:
    f_contents = f.read().splitlines()

# Part 1
def part1(*args):
    valid_pass_count = 0
    keycount = 0  # number of keys, need 7 wihout [cid] for pass to be valid
    for line in f_contents:
        if line == "":  # new entry seperated by an empty line
            if keycount == len(args):  # check if entry has 7 keys
                valid_pass_count += 1
            keycount = 0  # reset key count for next entry
            continue
        for field in line.split():
            key, value = field.split(
                ":"
            )  # split field into key and value, used to count keys ignoring [cid]
            if key in args:
                keycount += 1
    return valid_pass_count


print(part1("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"))

# Part 2
def validation(key, value):
    if key == "byr" and (1920 <= int(value) <= 2020):
        return True
    if key == "iyr" and (2010 <= int(value) <= 2020):
        return True
    if key == "eyr" and (2020 <= int(value) <= 2030):
        return True
    if key == "hgt" and "cm" in value and (150 <= int(value[:-2]) <= 193):
        return True
    if key == "hgt" and "in" in value and (59 <= int(value[:-2]) <= 76):
        return True
    if key == "hcl" and re.match(r"^#[0-9a-f]{6}", value) is not None:
        return True
    if key == "ecl" and value in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth"):
        return True
    if key == "pid" and len(value) == 9:
        return True

    return False


def part2():
    fields = ("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid")
    valid_pass_count = 0
    keycount = 0  # number of keys, need 7 wihout [cid] for pass to be valid
    for line in f_contents:
        if line == "":  # new entry seperated by an empty line
            if keycount == len(fields):  # check if entry has 7 keys
                valid_pass_count += 1
            keycount = 0  # reset key count for next entry
            continue
        for field in line.split():
            key, value = field.split(
                ":"
            )  # split field into key and value, used to count keys ignoring [cid]
            if key in fields:
                if validation(key, value):
                    keycount += 1
    return valid_pass_count


print(part2())