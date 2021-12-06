import os
import datetime

here = os.path.abspath(os.path.curdir)
proj = 'AoC2021'
infile = 'p06_input.txt'
# infile = 'p06_testinput.txt'

infile_path = os.path.join(here, proj, infile)
print(infile_path, os.path.exists(infile_path))

def part1(): # list comprehension == super duper slow
    '''day 6 part 1'''

    fishy_school = []
    max_days = 80

    def fish_spawner():
        if 0 in fishy_school:
            for fish in fishy_school:
                if fish == 0:
                    # padding age by 1 since new list generation will reduce it
                    fishy_school.append(9)

    with open(infile_path, 'r') as f:
        line = f.readline()
        fishy_school = [int(age) for age in line.strip().split(',')]

    for _ in range(max_days):
        fish_spawner()
        fishy_school = [age - 1 if age > 0 else age + 6 for age in fishy_school]

    return len(fishy_school)

def part2():
    '''day 6 part 2'''
    max_days = 256

    fish_ages = {'8':0, '7':0, '6':0, '5':0, '4':0, '3':0, '2':0, '1':0, '0':0}
    temp_set = fish_ages.copy()

    with open(infile_path, 'r') as f:
        fishy_school = (age for age in f.readline().strip().split(','))

        for age in fishy_school:
            fish_ages[age] += 1

    for _ in range(max_days):
        for age in (str(age) for age in range(len(fish_ages) - 1, -1, -1)):
            if age != '0':
                temp_set[str(int(age) - 1)] = fish_ages[age]
            else:
                temp_set['8'] = fish_ages[age]
                temp_set['6'] += fish_ages[age]
        fish_ages = temp_set.copy()

    num_fish = 0
    counts = (count for _, count in fish_ages.items())
    for c in counts:
        num_fish += c
    return num_fish


if __name__ == "__main__":
    start1 = datetime.datetime.now()
    ans1 = part1()
    end1 = datetime.datetime.now()
    print('part 1 answer {}'.format(ans1))
    print('took: {}'.format(end1 - start1))

    start2 = datetime.datetime.now()
    ans2 = part2()
    end2 = datetime.datetime.now()
    print('part 2 answer {}'.format(ans2))
    print('took: {}'.format(end2 - start2))