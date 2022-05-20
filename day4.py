#https://adventofcode.com/2020/day/4
'''
Lessons learnt:
Key value pairs screams dict but the data is structured well enough that it's not required. I found a simple list was easier to work with.
'''
import re
data = open('input4.txt', 'r').read().split("\n\n")


def part_one():
    required = ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid')
    valid = 0
    for line in data:
        if all(x in line for x in required):
            valid += 1
    return valid

def got_required(string):
    required = ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid')
    if all(x in string for x in required):
        return True

def valid_byr(birth_year):
    return 1920 <= int(birth_year) <= 2002

def valid_iyr(issue_year):
    return 2010 <= int(issue_year) <= 2020

def valid_expiry(exp_year):
    return 2020 <= int(exp_year) <= 2030

def valid_height(height):
    num = int(re.search(r'\d+', height).group())
    if 'in' in height:
        return 59 <= num <= 76
    elif 'cm' in height:
        return 150 <= num <= 193

def valid_hair(hair_colour):
    regex = '^#([a-f0-9]{6})$'
    p = re.compile(regex)
    if (re.search(p, hair_colour)):
        return True

def valid_eye(eye_colour):
    valid_colours = ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth')
    return eye_colour in valid_colours

def valid_pid(pid):
    if len(pid) == 9 and pid.isdigit():
            return True


def valid_passports():
    valid = []
    passport_valid = 0
    for line in data:
        if got_required(line):
            valid.append(line.replace('\n', ' '))
    for passport in valid:
        fields = passport.split(" ")
        byr, iyr, eyr, hgt, hcl, ecl, pid = (False,) * 7
        for field in fields:
            item = field.split(":")
            if item[0] == 'byr' and valid_byr(item[1]):
                byr = True
            elif item[0] == 'iyr' and valid_iyr(item[1]):
                iyr = True
            elif item[0] == 'eyr' and valid_expiry(item[1]):
                eyr = True
            elif item[0] == 'hgt' and valid_height(item[1]):
                hgt = True
            elif item[0] == 'hcl' and valid_hair(item[1]):
                hcl = True
            elif item[0] == 'ecl' and valid_eye(item[1]):
                ecl = True
            elif item[0] == 'pid' and valid_pid(item[1]):
                pid = True
        if byr and iyr and eyr and hgt and hcl and ecl and pid:
            passport_valid += 1
    return passport_valid

print(valid_passports())