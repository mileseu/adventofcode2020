#https://adventofcode.com/2020/day/5
'''
Lessons learnt:

'''
data = open('input5.txt', 'r').read().split("\n")

def row_number(boarding_pass):
    row = [x for x in range(128)]
    for letter in boarding_pass[:7]:
        length = len(row)
        if letter == "F":
            #keep lower half
            row = row[:int(length/2)]
        if letter == "B":
            #keep upper half
            row = row[int(length/2):]
    return row[0]

def column_number(boarding_pass):
    column = [x for x in range(8)]
    for letter in boarding_pass[-3:]:
        length = len(column)
        if letter == "L":
            #keep lower half
            column = column[:int(length/2)]
        if letter == "R":
            #keep upper half
            column = column[int(length/2):]
    return column[0]

all_tickets = []
def part_one():
    for ticket in data:
        seat_row = row_number(ticket)
        seat_column = column_number(ticket)
        all_tickets.append(seat_row * 8 + seat_column)
    return max(all_tickets)
print(part_one())

def part_two():
    part_one()
    for i in range(min(all_tickets), max(all_tickets)):
        if i not in all_tickets:
            my_ticket = i
    return my_ticket
print(part_two())