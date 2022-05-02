#https://adventofcode.com/2020/day/2
'''
Lessons learnt:
Regex in Python, separated by | https://www.w3schools.com/python/python_regex.asp
count() method https://www.programiz.com/python-programming/methods/string/count
'''

import re
#open text file, read mode | read file and split by new line
data = open('input2.txt', 'r').read().split('\n')

#split the strings in data by: lower number, higher number, letter, password
split_data = []
for i in range(len(data)):
    split_data.append(re.split('-|\s|:\s', data[i]))


#if the password contains the letter between lower and higher number it is valid 
def valid_passwords():
    valid = 0
    for list in split_data:
        #count occurrences of letter in password
        count = list[3].count(list[2])
        if count >= int(list[0]) and count <= int(list[1]):
            valid += 1
    print(valid)

#at index lower and higher (-1 to correct to 0 index) if the password character matches only 1 then valid
def part_two_valid_passwords():
    valid = 0
    not_valid = 0
    #go through each entry
    for list in split_data:
        #set indexes
        low_index = int(list[0])-1
        high_index = int(list[1])-1
        password_low_index = list[3][low_index]
        password_high_index = list[3][high_index]

        #set match patterns
        if password_low_index == list[2] or password_high_index == list[2]:
            if password_low_index == list[2] and password_high_index == list[2]:
                not_valid += 1
            else:
                valid +=1
    print(valid)
    print(not_valid)

    

part_two_valid_passwords()