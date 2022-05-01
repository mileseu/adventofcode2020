data = open('input1.txt', 'r').read().split('\n')

data = list(map(lambda number: int(number), data))

searching = True
results = []

while searching:
    last_number = data.pop()

    for number in data:
        if number + last_number == 2020:
            results.append(number * last_number)
            searching = False

        if len(data) < 1:
            searching = False

print(results)