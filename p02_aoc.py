import os

def puz01():
    curdir = os.path.abspath(os.path.curdir)
    proj = 'aoc'
    infile = 'p02_input.txt'

    infile_path = os.path.join(curdir, proj, infile)

    h_pos = 0
    v_pos = 0

    with open(infile_path, 'r') as f:
        lines = f.readlines()

        for line in lines:
            (dir, pos) = line.split(' ')
            pos = int(pos)

            if dir == 'forward':
                h_pos += pos
                print('move forward {0} to pos {1}'.format(pos, h_pos))
            if dir == 'up':
                v_pos -= pos
                print('move up {0} to depth {1}'.format(pos, v_pos))
            if dir == 'down':
                v_pos += pos
                print('move down {0} to depth {1}'.format(pos, v_pos))
    print(h_pos, v_pos)
    print('answer: {}'.format(h_pos * v_pos))

def puz02():
    curdir = os.path.abspath(os.path.curdir)
    proj = 'aoc'
    infile = 'p02_input.txt'

    infile_path = os.path.join(curdir, proj, infile)

    h_pos = 0
    v_pos = 0
    aim = 0

    with open(infile_path, 'r') as f:
        lines = f.readlines()

        for line in lines:
            (dir, pos) = line.split(' ')
            pos = int(pos)

            if dir == 'forward':
                h_pos += pos
                v_pos += (aim * pos)
                print('move forward {0} to pos {1} and a new depth of {2}'.format(pos, h_pos, v_pos))
            if dir == 'up':
                aim -= pos
                print('adjust aim shallower to {0}'.format(aim))
            if dir == 'down':
                aim += pos
                print('adjust aim deeper to {0}'.format(aim))
    print(h_pos, v_pos)
    print('answer: {}'.format(h_pos * v_pos))

if __name__ == "__main__":
    # puz01()
    puz02()