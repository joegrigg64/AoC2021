import os
import time

here = os.path.abspath(os.path.curdir)
project = 'AoC2021'
infile = 'p07_input.txt'
# infile = 'p07_testinput.txt'

infile_path = os.path.join(here, project, infile)

def part1():

    sub_positions = []
    max_p = 0
    min_p = 0
    min_fuel_taken = None

    with open(infile_path, 'r') as f:
        pos_gen = (int(p) for p in f.readline().strip().split(','))

        sub_positions = list(pos_gen)

    gen_max = (n for n in sub_positions)
    max_p = max(gen_max)

    gen_min = (n for n in sub_positions)
    min_p = min(gen_min)

    for n in range(min_p, max_p + 1):
        fuel_taken = 0
        gen_fuel = (abs(n - p) for p in sub_positions)

        for f_val in gen_fuel:
            fuel_taken += f_val

        if min_fuel_taken == None:
            min_fuel_taken = fuel_taken
        else:
            min_fuel_taken = fuel_taken if fuel_taken < min_fuel_taken else min_fuel_taken

    return min_fuel_taken

def part2():

    sub_positions = []
    max_p = 0
    min_p = 0
    min_fuel_taken = None

    with open(infile_path, 'r') as f:
        pos_gen = (int(p) for p in f.readline().strip().split(','))

        sub_positions = list(pos_gen)

    max_p = max(sub_positions)
    min_p = min(sub_positions)

    for n in range(min_p, max_p + 1):
        fuel_taken = 0
        gen_fuel = (abs(n - p) for p in sub_positions)

        for dist in gen_fuel:
            this_sub_fuel = 0
            last_val = 0
            next_val = 0
            for _ in range(dist + 1):
                next_val = _
                this_sub_fuel = next_val + last_val
                last_val = this_sub_fuel

            fuel_taken += this_sub_fuel

        if min_fuel_taken == None:
            min_fuel_taken = fuel_taken
        else:
            min_fuel_taken = fuel_taken if fuel_taken < min_fuel_taken else min_fuel_taken

    return min_fuel_taken

if __name__ == "__main__":
    start1 = time.time()
    ans1 = part1()
    end1 = time.time()
    print(f'part 1 answer: {ans1}')
    print(f'part 1 took: {end1 - start1}')

    start2 = time.time()
    ans2 = part2()
    end2 = time.time()
    print(f'part 2 answer: {ans2}')
    print(f'part 2 took: {end2 - start2}')