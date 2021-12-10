import os
import time

here = os.path.abspath(os.path.curdir)
project = 'aoc'
# infile = 'p09_testinput.txt'
infile = 'p09_input.txt'

infile_path = os.path.join(here, project, infile)

basin_size = 0

def computeStuff():
    '''dat 9'''

    risk_level = 0

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
                global basin_size
                basin_size += 1
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

                risk_level += (lines[i][j]+1)

                global basin_size
                basin_size = 1
                points = [[i, j]]
                basinBuilder(i, j, points)
                basins.append(basin_size)

    answer2 = 1
    for n in sorted(basins)[-3:]:
        answer2 *= n
    return (risk_level, answer2)

if __name__ == "__main__":
    start = time.time()
    (ans1, ans2) = computeStuff()
    print(f'part 1: {ans1}, part 2: {ans2}')
    print(f'took: {time.time() - start}')