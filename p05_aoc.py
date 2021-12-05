import os
import re

here = os.path.abspath(os.path.curdir)
project = 'AoC2021'
infile = 'p05_input.txt'

infile_path = os.path.join(here, project, infile)


def part1():
    '''day 5 part 1'''

    diagram = []
    diagram_line = []
    max_x = 0
    max_y = 0
    coords = []

    with open(infile_path, 'r') as f:
        lines = f.readlines()

        # get coords and diagram dimensions
        for line in lines:
            '''do things here'''
            (coord1, coord2) = line.split(' -> ')
            (x1, y1) = coord1.split(',')
            (x2, y2) = coord2.split(',')

            if x1 != x2 and y1 != y2:
                continue

            x1 = int(x1)
            x2 = int(x2)
            y1 = int(y1)
            y2 = int(y2)

            max_x = x1 if x1 > max_x else max_x
            max_x = x2 if x2 > max_x else max_x
            max_y = y1 if y1 > max_y else max_y
            max_y = y2 if y2 > max_y else max_y

            coords.append([[x1, y1], [x2, y2]])
            # print(coords)

    # build diagram
    for _ in range(max_x + 1): # account for 0 and top range non-inclusive
        diagram_line.append('.')

    for _ in range(max_y + 1):
        diagram.append(diagram_line)

    print(len(diagram_line), len(diagram), max_x, max_y)
    print(diagram[max_y][max_x])

    # print(len(diagram), max_x)
    # print(diagram[990])

    for cl in coords:
        # print(cl)
        if cl[0][0] == cl[1][0]: # even x
            x = cl[0][0]
            #TODO: fix setting y range and x range below
            print(cl, x)
            for y in range(cl[0][1], cl[1][1]):
                # print(diagram[y], len(diagram[y]))
                if diagram[y][cl[0][0]] == '.':
                    diagram[y][cl[0][0]] = '1'
                else:
                    diagram[y][cl[0][0]] = str(int(diagram[y][cl[0][0]]) + 1)

        if cl[0][1] == cl[1][1]: # even y
            for x in range(cl[0][0], cl[1][0]):
                if diagram[cl[0][1]][x] == '.':
                    diagram[cl[0][1]][x] = '1'
                else:
                    diagram[cl[0][1]] = str(int(diagram[cl[0][1]][x]) + 1)
    
    # print(diagram)
                    

    return 'not done yet with part 1'

def part2():
    '''day 5 part 2'''

    with open(infile_path, 'r') as f:
        lines = f.readlines()

        for line in lines:
            '''do things here'''

    return 'not done yet with part 2'

if __name__ == "__main__":
    answer1 = part1()
    print('part 1 answer: {}'.format(answer1))

    answer2 = part2()
    print('part 2 answer: {}'.format(answer2))