import os
import re
import datetime

here = os.path.abspath(os.path.curdir)
project = 'aoc'
infile = 'p05_input.txt'
# infile = 'p05_testinput.txt'

infile_path = os.path.join(here, project, infile)


def part1():
    '''day 5 part 1'''

    diagram = []
    diagram_line = []
    max_x = 0
    max_y = 0
    coords = []
    overlap_over2 = 0

    with open(infile_path, 'r') as f:
        lines = f.readlines()
        c = 0
        # get coords and diagram dimensions
        for line in lines:
            c += 1
            '''do things here'''
            (coord1, coord2) = line.split(' -> ')
            (x1, y1) = coord1.split(',')
            (x2, y2) = coord2.split(',')

            if (x1.strip() != x2.strip()) and (y1.strip() != y2.strip()):
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

    # build diagram
    for _ in range(max_x + 1): # account for 0 and top range non-inclusive
        diagram_line.append('.')

    for _ in range(max_y + 1):
        diagram.append(diagram_line.copy())

    for cl in coords:
        if cl[0][0] == cl[1][0]: # even x
            x = cl[0][0]
            y_start = cl[0][1] if cl[0][1] < cl[1][1] else cl[1][1]
            y_end = cl[1][1] if cl[1][1] > cl[0][1] else cl[0][1]

            for y in range(y_start, y_end + 1):
                if diagram[y][x] == '.':
                    diagram[y][x] = '1'
                else:
                    diagram[y][x] = str(int(diagram[y][x]) + 1)

        if cl[0][1] == cl[1][1]: # even y
            y = cl[0][1]
            x_start = cl[0][0] if cl[0][0] < cl[1][0] else cl[1][0]
            x_end = cl[1][0] if cl[1][0] > cl[0][0] else cl[0][0]

            for x in range(x_start, x_end + 1):
                if diagram[y][x] == '.':
                    diagram[y][x] = '1'
                else:
                    diagram[y][x] = str(int(diagram[y][x]) + 1)

    for row in diagram:
        for dot in row:
            if dot == '.':
                continue
            else:
                if int(dot) >= 2:
                    overlap_over2 += 1
    return overlap_over2

def part2():
    '''day 5 part 2'''

    diagram = []
    diagram_line = []
    max_x = 0
    max_y = 0
    coords = []
    overlap_over2 = 0

    with open(infile_path, 'r') as f:
        lines = f.readlines()
        c = 0
        # get coords and diagram dimensions
        for line in lines:
            c += 1
            '''do things here'''
            (coord1, coord2) = line.split(' -> ')
            (x1, y1) = coord1.split(',')
            (x2, y2) = coord2.split(',')

            x1 = int(x1)
            x2 = int(x2)
            y1 = int(y1)
            y2 = int(y2)

            max_x = x1 if x1 > max_x else max_x
            max_x = x2 if x2 > max_x else max_x
            max_y = y1 if y1 > max_y else max_y
            max_y = y2 if y2 > max_y else max_y

            coords.append([[x1, y1], [x2, y2]])

    # build diagram base
    for _ in range(max_x + 1): # account for 0 and top range non-inclusive
        diagram_line.append('.')

    for _ in range(max_y + 1):
        diagram.append(diagram_line.copy())

    # make lines in diagram
    for cl in coords:
        # horizontal line
        if cl[0][0] == cl[1][0]: # even x
            x = cl[0][0]
            y_start = cl[0][1] if cl[0][1] < cl[1][1] else cl[1][1]
            y_end = cl[1][1] if cl[1][1] > cl[0][1] else cl[0][1]

            for y in range(y_start, y_end + 1):
                if diagram[y][x] == '.':
                    diagram[y][x] = '1'
                else:
                    diagram[y][x] = str(int(diagram[y][x]) + 1)

        # vertical line
        elif cl[0][1] == cl[1][1]: # even y
            y = cl[0][1]
            x_start = cl[0][0] if cl[0][0] < cl[1][0] else cl[1][0]
            x_end = cl[1][0] if cl[1][0] > cl[0][0] else cl[0][0]

            for x in range(x_start, x_end + 1):
                if diagram[y][x] == '.':
                    diagram[y][x] = '1'
                else:
                    diagram[y][x] = str(int(diagram[y][x]) + 1)

        # is a diagonal line (always 45 deg)
        else:
            x1 = cl[0][0]
            x2 = cl[1][0]
            y1 = cl[0][1]
            y2 = cl[1][1]

            next_x = x1
            next_y = y1

            def make_mark(x, y):
                if diagram[next_y][next_x] == '.':
                    diagram[next_y][next_x] = '1'
                else:
                    diagram[next_y][next_x] = str(int(diagram[next_y][next_x]) + 1)            
            while next_x != x2: # 45 deg x and y have same rate of change
                make_mark(next_x, next_y)
                
                next_x += 1 if x2 > next_x else -1
                next_y += 1 if y2 > next_y else -1

            # set last mark since my while loop hasn't had enough coffee and skips it
            make_mark(x2, y2)

    # count intersections
    for row in diagram:
        for dot in row:
            if dot == '.':
                continue
            else:
                if int(dot) >= 2:
                    overlap_over2 += 1

    return overlap_over2

if __name__ == "__main__":
    now1 = datetime.datetime.now()
    answer1 = part1()
    future1 = datetime.datetime.now()
    print('part 1 answer: {}'.format(answer1))
    print('took {}'.format(future1 - now1))

    now2 = datetime.datetime.now()
    answer2 = part2()
    future2 = datetime.datetime.now()
    print('part 2 answer: {}'.format(answer2))
    print('took {}'.format(future2 - now2))