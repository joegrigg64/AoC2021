import os
import time

infile = 'p14_input.txt'
# infile = 'p14_testinput.txt'
infile_dir = os.path.join(os.path.abspath(os.path.curdir), 'AoC2021', infile)

def day14():
    # I -- 2d array of pair with insert type
    P = {}
    P_i = {}
    # extra_trailing_char -- store final char to be counted

    with open(infile_dir, 'r') as f:
        perm = f.readline().strip()
        extra_trailing_char = perm[-1]
        _ = f.readline()

        SEQ = [[c for c in line.strip().split(' -> ')] for line in f.readlines()]

    # build original counts of pairs
    for i, c in enumerate(perm):
        if i > 0:
            char = perm[i-1]+c
            P[char] = P[char] + 1 if char in P else 1

    for _ in range(40): # 10 for part 1
        for seq in SEQ:
            if seq[0] in P:
                s1 = seq[0][0]+seq[1]
                s2 = seq[1]+seq[0][1]
                P_i[s1] = P_i[s1] + P[seq[0]] if s1 in P_i else P[seq[0]]
                P_i[s2] = P_i[s2] + P[seq[0]] if s2 in P_i else P[seq[0]]
        P = P_i
        P_i = {}

    Chars = {}
    for k,v in P.items():
        Chars[k[0]] = Chars[k[0]] + v if k[0] in Chars else v

    Chars[extra_trailing_char] += 1
    high = max([v for k,v in Chars.items()])
    low = min([v for k,v in Chars.items()])
    difference = high - low

    return ('not computing', difference)

if __name__ == "__main__":
    start = time.time()
    (ans1, ans2) = day14()
    print(f'part 1: {ans1}, part 2: {ans2}, took: {time.time() - start}')