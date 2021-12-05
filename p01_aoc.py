import os

here = os.path.abspath(os.path.curdir)
infile = "p01_input.txt"
proj = "AoC2021"
infile_path = os.path.join(here, proj, infile)

def main():
    inc_count = 0
    with open(infile_path, 'r') as f:
        lines = f.readlines()

        for i, line in enumerate(lines):
            if i > 3: # part 1 -- i > 1
                # if int(line) > int(lines[int(index) - 1]): # part1
                prev_sum = sum([int(lines[i-1]), int(lines[i-2]), int(lines[i-3])])
                curr_sum = sum([int(lines[i]), int(lines[i-1]), int(lines[i-2])])
                if curr_sum > prev_sum:
                    inc_count += 1

    print(inc_count)

if __name__ == "__main__":
    main()