import os
import time

here = os.path.abspath(os.path.curdir)
proj = 'aoc'
# infile = 'p08_testinput.txt'
infile = 'p08_input.txt'

infile_path = os.path.join(here, proj, infile)

def part1():
    '''day 8 part 1'''

    unique_lengths = [2, 3, 4, 7]

    with open(infile_path, 'r') as f:
        lines = f.readlines()

        unique_digit_count = 0

        for line in lines:
            output = line.split(' | ')[-1].strip()
            digits = output.split(' ')
            for digit in digits:
                if len(digit) in unique_lengths:
                    unique_digit_count += 1


    return unique_digit_count


#stuff for part 2
orig_digit_perms = { # lengths
    '0': 'abcefg',     # 6
    '1': 'cf',         # 2
    '2': 'acdeg',      # 5
    '3': 'acdfg',      # 5
    '4': 'bcdf',       # 4
    '5': 'abdfg',      # 5
    '6': 'abdefg',     # 6
    '7': 'acf',        # 3
    '8': 'abcdefg',    # 7
    '9': 'abcdfg'      # 6
}

dig_map = {}

def part2():
    '''day 8 part 2'''
    with open(infile_path, 'r') as f:
        lines = f.readlines()

    answer = 0

    for line in lines:
        digit_map = {} # line: original
        (digit_perms, output_perms) = (s.strip().split(' ') for s in line.strip().split(' | '))

        # 1 vals
        c_f = ''.join(sorted(next((p for p in digit_perms if len(p) == 2))))

        # remaining vals in 4
        b_d = ''.join(sorted([c for c in next((p for p in digit_perms if len(p) == 4)) if c not in c_f]))

        # set outlyer in 7
        mapped_a = next((c for c in next((p for p in digit_perms if (len(p) == 3))) if c not in c_f))
        digit_map[mapped_a] = 'a'

        # remaining vals bottom left of 8
        e_g = ''.join([c for c in next((p for p in digit_perms if len(p) == 7)) if (c not in c_f) and (c not in b_d) and (c not in digit_map)])

        # find single match in e_g with 5 or 3 which will only match one and the same of e_g
        # also find single match from b_d from 2 or 3 for the same reason
        # 2 will match only one c_f and both e_g - can use that to pin point c_f
        for p in [p for p in digit_perms if len(p) == 5]:
            e_g_matches = []
            b_d_matches = []
            c_f_matches = []
            for c in p:
                # if c not in c_f and c not in b_d and c not in digit_map:
                if c in e_g:
                    e_g_matches.append(c)
                if c in b_d:
                    b_d_matches.append(c)
                if c in c_f:
                    c_f_matches.append(c)

            # take care of c_f first due to double match criteria coming from 2
            if len(e_g_matches) == 2 and len(c_f_matches) == 1:
                digit_map[c_f_matches[0]] = 'c'
                temp_c_f = c_f.replace(c_f_matches[0], '')
                digit_map[temp_c_f] = 'f'

            if len(e_g_matches) == 1:
                digit_map[e_g_matches[0]] = 'g'
                temp_e_g = e_g.replace(e_g_matches[0], '')
                digit_map[temp_e_g] = 'e'

            if len(b_d_matches) == 1:
                digit_map[b_d_matches[0]] = 'd'
                temp_b_d = b_d.replace(b_d_matches[0], '')
                digit_map[temp_b_d] = 'b'

        assert len(digit_map) == 7

        # convert output permutations to original then compute
        output_num = ''
        for p in output_perms:
            o_perm = ''
            for c in p:
                o_perm += digit_map[c]
            output_num += [k for k, v in orig_digit_perms.items() if v == ''.join(sorted(o_perm))][0]

        answer += int(output_num)
    return answer

if __name__ == "__main__":
    s1 = time.time()
    print(f'part 1: {part1()}')
    print(f'took: {time.time() - s1}')

    s2 = time.time()
    print(f'part 2: {part2()}')
    print(f'took: {time.time() - s2}')