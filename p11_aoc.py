# from queue import LifoQueue as LQ
import os
import time

here = os.path.abspath(os.path.curdir)
project = 'aoc'
infile = 'p11_testinput.txt'
# infile = 'p11_input.txt'

infile_path = os.path.join(here, project, infile)

def day11():
    '''day 11'''

    with open(infile_path, 'r') as f:
        # lines = f.readlines()
        flashes = 0

        O = [[int(c) for c in [*line.strip()]] for line in f.readlines()]
        print(O)

        # for step in range(100):
        do_flash = []

        def flash(y, x):
            if y != 0:

            if x != 0:

        for y in range(len(O)):
            for x in range(len(O[y])):
                O[y][x] += 1
                if O[y][x] >= 9:
                    do_flash.append([y, x])

    print(O)
    print(do_flash)
    return ('not done', 'not done')


if __name__ == "__main__":    
    start = time.time()
    (ans1, ans2) = day11()
    print(f'part 1: {ans1}, part 2: {ans2}, took: {time.time() - start}')    