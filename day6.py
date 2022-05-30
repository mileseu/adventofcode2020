#https://adventofcode.com/2020/day/6
'''
Lessons learnt:
sets and set intersections using Python
'''
def read_input():
    return open('input6.txt', 'r').read().split("\n\n")
data = read_input()


def part_one():
    new_data = [x.replace('\n','') for x in data]
    total_count = 0
    for line in new_data:
        count = len(set(line))
        total_count += count
    return total_count

print(part_one())

def part_two():
    groups = [line.splitlines() for line in data]
    count = 0

    for group in groups:
        if len(group) == 1:
            count += len(group[0])
        else:
            intersection_of_answers = set(group[0]).intersection(*group[1:])
            count += len(intersection_of_answers)

    return count

print(part_two())