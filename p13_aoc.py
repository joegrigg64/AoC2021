import os
import time
import re

infile = 'p13_input.txt'
# infile = 'p13_testinput.txt'
infile_dir = os.path.join(os.path.abspath(os.path.curdir), 'aoc', infile)

def day13():

    p1 = 0
    folds = []
    # coords = [] 2d list of coordinates [x, y] -- created below

    with open(infile_dir, 'r') as f:
        lines = f.readlines()

    instruction_break = lines.index('\n')
    coords = [[int(c) for c in line.strip().split(',')] for line in lines[:instruction_break]]
    folds_lines = [re.search(r'^fold along (.*)', line).groups()[0] for line in lines[instruction_break+1:]]
    
    # listify the fold instructions
    for F in folds_lines:
        [I, L] = [c for c in F.strip().split('=')]
        folds.append([0 if I == 'x' else 1, int(L)])

    fold_count = 0
    for F in folds:
        if fold_count == 1:
            p1 = len(coords)
        for C in [C for C in coords if C[F[0]] > F[1]]:
            N = C[F[0]]
            C[F[0]] = N - (2*(N-F[1]))
            while coords.count(C) > 1:
                del coords[coords.index(C)]
        fold_count += 1

    #part 2
    W = 0
    H = 0
    for C in coords:
        W = C[0] if C[0] > W else W
        H = C[1] if C[1] > H else H
    
    print(W, H)
    paper = []
    for h in range(H+1):
        row = []
        for w in range(W+1):
            row.append('#' if [w, h] in coords else '.')
        paper.append(''.join(row))
    print('\n'.join(paper))

    return (p1, 'see fine print')

if __name__ == "__main__":
    start = time.time()
    (ans1, ans2) = day13()
    print(f'part 1: {ans1}, part 2: {ans2}, took: {time.time() - start}')