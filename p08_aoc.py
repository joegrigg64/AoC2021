import os
import time

here = os.path.abspath(os.path.curdir)
proj = 'aoc'
infile = 'p08_testinput.txt'
# infile = 'p08_input.txt'

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

def part2():
    '''day 8 part 2'''

    digit_sum = 0
    original_digits = {'abcefg': '0', 'cf': '1', 'acdeg': '2', 'acdfg': '3', 'bcdf': '4', 'abdfg': '5', 'abdefg': '6', 'acf': '7', 'abcdefg': '8', 'abcdfg': '9' }
    segment_mapper = {'a': '', 'b': '', 'c': '', 'd': '', 'e': '', 'f': '', 'g': ''}

    def decoder(corrupt_digits):
        '''maybe do some decoding to solve this thing'''
        d_map = {}

        return d_map

    with open(infile_path, 'r') as f:
        lines = f.readlines()

        for line in lines:
            output_num = ''
            (corrupt_digits, output) = line.strip().split(' | ')
            corrupt_digits = corrupt_digits.strip().split(' ')
            out_digits = output.strip().split(' ')
            d_map = decoder(corrupt_digits)
            for digit in out_digits:
                if ''.join(sorted(digit)) in d_map:
                    output_num += d_map[digit]
            digit_sum += int(output_num)

    return 'not done'

if __name__ == "__main__":
    print(f'part 1 {part1()}')

    print(f'part 2 {part2()}')