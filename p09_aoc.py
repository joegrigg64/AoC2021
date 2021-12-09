import os
import time

here = os.path.abspath(os.path.curdir)
project = 'AoC2021'
# infile = 'p09_testinput.txt'
infile = 'p09_input.txt'

infile_path = os.path.join(here, project, infile)

def part1():
    '''day 9 part 1'''

    risk_level = 0

    with open(infile_path, 'r') as f:
        lines = [[int(i) for i in [*line.strip()]] for line in f.readlines()]

    # directions return True if value exists and is higher, or doesn't exist (assumed higher since checking val is on an edge)
    def up(i, j):
        if i == 0:
            return True
        return lines[i-1][j] > lines[i][j]

    def left(i, j):
        if j == 0:
            return True
        return lines[i][j-1] > lines[i][j]
    
    def right(i, j):
        try:
            return lines[i][j+1] > lines[i][j]
        except:
            return True

    def down(i, j):
        try:
            return lines[i+1][j] > lines[i][j]
        except:
            return True

    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if up(i, j) and left(i, j) and right(i, j) and down(i, j):
                risk_level += (lines[i][j]+1)

    return risk_level



basin = 0

def part2():
    '''dat 9 part 2'''
    with open(infile_path, 'r') as f:
        lines = [[int(i) for i in [*line.strip()]] for line in f.readlines()]

    # directions return True if value exists and is higher, or doesn't exist (assumed higher since checking val is on an edge)
    def down(i, j, points=None):
        try:
            is_higher = lines[i+1][j] > lines[i][j]
            if points is not None and lines[i+1][j] < 9 and [i+1, j] not in points:
                global basin
                basin += 1
                points.append([i+1, j])                    
                basinBuilder(i+1, j, points)

            return is_higher
        except:
            return True

    def left(i, j, points=None):
        if j == 0:
            return True

        is_higher = lines[i][j-1] > lines[i][j]
        if points is not None and lines[i][j-1] < 9 and [i, j-1] not in points:
            global basin
            basin += 1
            points.append([i, j-1])                
            basinBuilder(i, j-1, points)

        return is_higher
    
    def right(i, j, points=None):
        try:
            is_higher = lines[i][j+1] > lines[i][j]
            if points is not None and lines[i][j+1] < 9 and [i, j+1] not in points:
                global basin
                basin += 1
                points.append([i, j+1])
                basinBuilder(i, j+1, points)

            return is_higher
        except:
            return True

    def up(i, j, points=None):
        if i == 0:
            return True

        is_higher = lines[i-1][j] > lines[i][j]
        if points is not None and lines[i-1][j] < 9 and [i-1, j] not in points:
            global basin
            basin += 1
            points.append([i-1, j])
            basinBuilder(i-1, j, points)

        return is_higher

    def basinBuilder(i, j, points):
        up(i, j, points)
        left(i, j, points)
        right(i, j, points)
        down(i, j, points)

    basins = []

    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if up(i, j) and left(i, j) and right(i, j) and down(i, j):

                global basin
                basin = 1
                points = [[i, j]]
                basinBuilder(i, j, points)
                basins.append(basin)

    answer = 1
    for n in sorted(basins)[-3:]:
        answer *= n
    return answer

if __name__ == "__main__":
    s1 = time.time()
    print(f'part 1 : {part1()}')
    print(f'took: {time.time() - s1}')

    s2 = time.time()
    print(f'part 2 : {part2()}')
    print(f'took: {time.time() - s2}')