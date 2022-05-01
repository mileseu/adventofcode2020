#https://adventofcode.com/2020/day/1

#open text file, read mode | read file and split by new line
data = open('input1.txt', 'r').read().split('\n')
#map current list to ints
data = list(map(lambda number: int(number), data))

def two_numbers():
    searching = True

    while searching:
        last_number = data.pop()

        for number in data:
            if number + last_number == 2020:
                answer = number * last_number
                searching = False
                return answer

            if len(data) < 1:
                searching = False

#part two
def three_numbers():
    searching = True
    while searching:
        last_number = data.pop()

        for number in data:
            for number2 in data:
                if number + number2 + last_number == 2020 and number != number2:
                    answer = number * number2 * last_number
                    searching = False
                    return answer

            if len(data) < 2:
                searching = False

print(three_numbers())