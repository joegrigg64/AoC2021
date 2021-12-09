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

    def direction(dir, i, j, points=None):
        '''slightly slower than separate methods, but less code'''
        if dir == 'u':
            if i == 0:
                return True
            (i_n, j_n) = (i - 1, j)
        elif dir == 'l':
            if j == 0:
                return True
            (i_n, j_n) = (i, j - 1)
        elif dir == 'r':
            (i_n, j_n) = (i, j + 1)
        elif dir == 'd':
            (i_n, j_n) = (i + 1, j)
        try:
            is_higher = lines[i_n][j_n] > lines[i][j]
            if points is not None and lines[i_n][j_n] < 9 and [i_n, j_n] not in points:
                global basin
                basin += 1
                points.append([i_n, j_n])                    
                basinBuilder(i_n, j_n, points)

            return is_higher
        except:
            return True

    def basinBuilder(i, j, points):
        direction('u', i, j, points)
        direction('l', i, j, points)
        direction('r', i, j, points)
        direction('d', i, j, points)

    basins = []

    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if direction('u', i, j) and \
                direction('l', i, j) and \
                direction('r', i, j) and \
                direction('d', i, j):

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