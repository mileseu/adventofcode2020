#https://adventofcode.com/2020/day/3
'''
Lessons learnt:
Use modulo to repeat over the string's length
'''
data = open('input3.txt', 'r').read().split('\n')
repeat = len(data[0])
tree = "#"

def slope_2_tree_count():
    #counting all the trees (#) you would encounter for the toboggan right 3, down 1:
    right = 3
    start = 0
    tree_count = 0
    #down 1
    for row in data:
        #repeat = 31 i.e. row[31] becomes row[0], [32]->[1], [33]->[2] 
        increment = start % repeat
        if row[increment] == tree:
            tree_count += 1
        #right 3
        start += right

    return tree_count


def all_slopes_tree_count(right, down):
    #part 2 has multiple toboggans, abstracted the method to include toboggan input
    start = 0
    tree_count = 0
    #x = down
    for x in range(0, len(data), down):
        increment = start % repeat
        if data[x][increment] == tree:
            tree_count +=1
        #right = right
        start += right

            
    return tree_count


def calculate_answer():
    part_two_input = ((1,1),(3,1),(5,1),(7,1),(1,2))
    answer = 1
    for input in part_two_input:
        answer *= all_slopes_tree_count(input[0], input[1])
    print(answer)


calculate_answer()