import os
import re

infile = 'p03_input.txt'
proj = 'aoc'
here = os.path.abspath(os.path.curdir)

infile_path = os.path.join(here, proj, infile)

def p01():
    '''puzzle 1'''
    vals = []
    gamma = ''
    epsilon = ''

    with open(infile_path, 'r') as f:
        lines = f.readlines()

        for i, line in enumerate(lines):
            for j, char in enumerate(line.split('\n')[0]):
                if i == 0:
                    vals.append([0,0])
                vals[j][int(char, 2)] += 1

    for e in vals:
        gamma += '0' if e[0] > e[1] else '1'
        epsilon += '0' if e[0] < e[1] else '1'

    print(gamma, epsilon)
    print(int(gamma, 2), int(epsilon, 2))
    print('product {}'.format(int(gamma, 2) * int(epsilon, 2)))


def p02():
    '''puzzle 2'''
    o2_co2 = ['', '']
    vals = []

    def biterator8000(bit_index, val_list, sensor):
        counter_of_bits = [0, 0]

        for val in (val.strip() for val in val_list):
            counter_of_bits[int(val[bit_index], 2)] += 1
        
        if sensor == 0:
            o2_co2[sensor] += '0' if counter_of_bits[0] > counter_of_bits[1] else '1'
        else:
            o2_co2[sensor] += '0' if counter_of_bits[0] <= counter_of_bits[1] else '1'

        print(o2_co2)
        print('vals len %s and counter %s' % (len(vals), counter_of_bits))

    with open(infile_path, 'r') as f:
        lines = f.readlines()
        bits_len = len(lines[0].strip())

        for x in range(len(o2_co2)):
            vals = lines
            for bit_index in range(bits_len):
                if len(vals) == 1:
                    o2_co2[x] = vals[0].strip()
                    break
                biterator8000(bit_index, vals, x)
                r = re.compile(r"^%s.*" % o2_co2[x])
                vals = list(filter(r.match, vals))

    print(o2_co2)
    print("product {}".format(int(o2_co2[0], 2) * int(o2_co2[1], 2)))            

if __name__ == "__main__":
    p02()