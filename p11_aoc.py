import os
import time

here = os.path.abspath(os.path.curdir)
project = 'aoc'
# infile = 'p11_testinput.txt'
infile = 'p11_input.txt'

infile_path = os.path.join(here, project, infile)

O = []
flashes = 0
all_octs = 0

def flash(y, x):
    global O
    global do_flash
    global flashes
    flashes += 1
    O[y][x] = -1
    y_adj = [-1, 0, 1]
    x_adj = [-1, 0, 1]

    for ya in y_adj:
        for xa in x_adj:
            yy = y + ya
            xx = x + xa
            if (0 <= yy < (len(O))) and (0 <= xx < len(O[0])) and (O[yy][xx] != -1):
                O[yy][xx] += 1
                if O[yy][xx] > 9:
                    flash(yy, xx)

def day11():
    '''day 11'''

    with open(infile_path, 'r') as f:
        global O
        global flashes
        global all_octs
        O = [[int(c) for c in [*line.strip()]] for line in f.readlines()]

        all_octs = len(O) * len(O[0])

        flashes = 0
        flashers = 0
        turn = 0

        while flashers < all_octs: # part 1 do for _ in range(100):
            turn += 1
            flashers = 0
            for y in range(len(O)):
                for x in range(len(O[y])):
                    O[y][x] += 1

            for y in range(len(O)):
                for x in range(len(O[0])):
                    if O[y][x] > 9:
                        O[y][x] = -1
                        flash(y, x)

            for y in range(len(O)):
                for x in range(len(O[0])):
                    if O[y][x] == -1:
                        flashers += 1
                        O[y][x] = 0

    return (flashes, turn)

if __name__ == "__main__":
    start = time.time()
    (ans1, ans2) = day11()
    print(f'part 1: {ans1}, part 2: {ans2}, took: {time.time() - start}')