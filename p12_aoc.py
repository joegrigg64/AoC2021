import os
import time
from collections import deque

here = os.path.abspath(os.path.curdir)
project = 'AoC2021'
# infile = 'p12_testinput_small.txt'
# infile = 'p12_testinput_med.txt'
# infile = 'p12_testinput_large.txt'
infile = 'p12_input.txt'

infile_path = os.path.join(here, project, infile)

caves = {}
path_count = 0
pathway = deque(['start'])
twice = ''

def follow(next_cave):
    global caves
    global path_count
    global pathway
    global twice

    pathway.append(next_cave)
    if next_cave.islower() and next_cave != 'end' and twice == '' and pathway.count(next_cave) == 2:
        twice = next_cave

    if next_cave == 'end':
        path_count += 1
        pathway.pop()
        return

    if next_cave.islower() and ((twice != next_cave and pathway.count(next_cave) > 1) or (twice == next_cave and pathway.count(next_cave) > 2)):
        pathway.pop()
        return

    for nnext_cave in caves[next_cave]:
        follow(nnext_cave)

    pathway.pop()
    if twice == next_cave and pathway.count(next_cave) == 1:
        twice = ''
    return

def day12():
    global caves
    global pathway
    global path_count

    with open(infile_path, 'r') as f:
        lines = f.readlines()

    for line in lines:
        [before, after] = line.strip().split('-')
        if after != 'end' and before != 'start':
            if after not in caves:
                caves[after] = []
            caves[after].append(before)
        if after != 'start' and before != 'end':
            if before not in caves:
                caves[before] = []
            caves[before].append(after)

    for next_cave in caves['start']:
        follow(next_cave)

    return ('not running', path_count)

if __name__ == "__main__":
    start = time.time()
    (ans1, ans2) = day12()
    print(f'part 1: {ans1}, part 2: {ans2}, took: {time.time() - start}')