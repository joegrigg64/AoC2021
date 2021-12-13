import os
import time

here = os.path.abspath(os.path.curdir)
project = 'aoc'
infile = 'p12_testinput_small.txt'
# infile = 'p12_testinput_med.txt'
# infile = 'p12_testinput_large.txt'
# infile = 'p12_input.txt'

infile_path = os.path.join(here, project, infile)

caves = {}
small_visited = []
small_visited_twice = []
paths = 0
good_paths = []
# pathing = [] # restart each run

def follow(next, psf):
    n_psf = psf.copy()
    n_psf.append(next)
    global caves
    global small_visited
    global paths
    global small_visited_twice
    global good_paths
    # global pathing

    if next == 'end':
        nn_psf = n_psf.copy()
        # nn_psf.append('end')
        if nn_psf not in good_paths:
            paths += 1
            good_paths.append(n_psf.copy())
            # print(f'stopped at {next}')
            # print(nn_psf)
            return
    # print(f'at: {next}')
    if next.islower():
        if next in small_visited:
            small_visited_twice.append(next)
        small_visited.append(next)

    # if next not in caves: # dead end
    #     # print(f'stopped at {next}')

    #     return
    # if next in caves:
    # print(f'next paths to check: {caves[next]}')
    placement = len(small_visited)
    # print(f'small_visited: {small_visited}')
    try:
        for N in caves[next]:
            # print(n_psf)
            # print(f'before removals: {small_visited}')
            small_visited = small_visited[:placement]
            for small_check in small_visited_twice:
                count = 0
                for small in small_visited:
                    if small == small_check:
                        count += 1
                # print(count)
                if count == 1:
                    # print(f'removed {small_check}')
                    # print(small_visited)
                    small_visited_twice.remove(small_check)
                    # print(small_visited, small_visited_twice)

            
            if N not in small_visited_twice:
                # print(f'going to {N} from {next}')
                follow(N, n_psf.copy())
    except:
        ''''''
    return


def day12():

    global caves
    global small_visited
    global small_visited_twice

    with open(infile_path, 'r') as f:
        lines = f.readlines()

        for line in lines:
            before = []
            after = []
            L = line.strip().split('-')
            before.append(L[0])
            after.append(L[1])
            for i, B in enumerate(before):
                if B not in caves and B != 'end':
                    caves[B] = []
                if after[i] != 'start' and B != 'end':
                    caves[B].append(after[i])
            # if B.isupper() and after[i] != 'end':
                if after[i] not in caves and after[i] != 'end' and B != 'start':
                    caves[after[i]] = [B]
                elif B != 'start' and after[i] != 'end' and B not in caves[after[i]]:
                    caves[after[i]].append(B)

    print(caves)

    for C in caves['start']:
        path_so_far = ['start']
        global pathing

        small_visited_twice = []
        if C.islower():
            small_visited = [C]
        else:
            small_visited = []
        # print(f'at front with {C}')
        placement = len(small_visited)
        
        for N in caves[C]:
            
            small_visited = small_visited[:placement]
            for small_check in small_visited_twice:
                count = 0
                for small in small_visited:
                    if small == small_check:
                        count += 1
                if count == 1:
                    small_visited_twice.remove(small_check)

            # print(f'deeping into {N}')
            # pathing = ['start', N]
            follow(N, path_so_far.copy())
        # follow(C)
        # print(pathing)

    

    # print(caves)



    # print(len(good_paths))
    # print(good_paths)
    # copy_good_paths = []
    # for path in good_paths:
    #     if path not in copy_good_paths:
    #         copy_good_paths.append(path)
    # print(len(copy_good_paths))
    all_starts = []
    new_good_paths = []
    for P in caves['start']:
        all_starts.append(['start', P])    
    for path in good_paths:
        print(f'compare {path[:2]} against {all_starts}')
        print(path[:2] in all_starts)
        if path[:2] in all_starts:
            new_good_paths.append(path)
    print(len(new_good_paths))
            
    
    return (paths, 'not done')



if __name__ == "__main__":
    start = time.time()
    (ans1, ans2) = day12()
    print(f'part 1: {ans1}, part 2: {ans2}, took: {time.time() - start}')