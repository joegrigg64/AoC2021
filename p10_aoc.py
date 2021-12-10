from queue import LifoQueue as LQ
import os
import time

here = os.path.abspath(os.path.curdir)
project = 'aoc'
# infile = 'p10_testinput.txt'
infile = 'p10_input.txt'

infile_path = os.path.join(here, project, infile)

def day10():
    '''day 10'''

    closer_map = {
        ')': {'opener': '(', 'points1': 3, 'points2': 1}, # part 1 - 3 pts | part 2 - 1 pt
        ']': {'opener': '[', 'points1': 57, 'points2': 2}, # part 1 - 57 pts | part 2 - 2 pts
        '}': {'opener': '{', 'points1': 1197, 'points2': 3}, # part 1 - 1197 pts | part 2 - 3 pts
        '>': {'opener': '<', 'points1': 25137, 'points2': 4}  # part 1 - 25137 pts | part 2 - 4 pts
    }

    opener_map = {
        '(': ')',
        '[': ']',
        '{': '}',
        '<': '>'
    }

    ans1 = 0
    ans2 = 0
    ans2_vals = []

    with open(infile_path, 'r') as f:
        lines = f.readlines()

        for line in (line.strip() for line in lines):
            q = LQ(len(line))

            is_corrupt = False
            for c in line:
                if c in closer_map and not is_corrupt:
                    if closer_map[c]['opener'] == q.get():
                        continue
                    else:
                        ans1 += closer_map[c]['points1']
                        is_corrupt = True
                        break
                else:
                    q.put(c)

            if q.qsize() > 0 and not is_corrupt: # line was left open
                pts = 0
                while q.qsize() > 0:
                    next_val = q.get()
                    pt_val = closer_map[opener_map[next_val]]['points2']
                    pts = (pts * 5) + pt_val
                ans2_vals.append(pts)

        middle = len(ans2_vals) // 2
        ans2 = sorted(ans2_vals)[middle]


    return (ans1, ans2)

if __name__ == "__main__":    
    start = time.time()
    (ans1, ans2) = day10()
    print(f'part 1: {ans1}, part 2: {ans2}, took: {time.time() - start}')