import os
import re

here = os.path.abspath(os.path.curdir)
project = 'aoc'
infile = 'p04_input.txt'

infile_path = os.path.join(here, project, infile)

class PuzzleBoard:
    column_count = 0
    row_count = 0
    tiles = [[]]
    unmarked_sum = 0
    last_marked = ''

    def __init__(self, tiles):
        '''tiles expects to be a 2 dimentional array of rows to columns where all rows have the same number of columns'''

        self.markers = {}
        self.iWonAlready = False
        self.tiles = tiles
        self.row_count = len(self.tiles)
        self.column_count = len(self.tiles[0])

        for row in self.tiles:
            for column_val in row:
                self.markers[column_val] = ''

    def markTile(self, num):
        self.markers[num] = 'x'
        self.last_marked = num

    def checkWinner(self):
        col_marks = []
        for _ in range(self.column_count):
            col_marks.append(0)

        for row in self.tiles:
            row_marks = 0
            for i, col_val in enumerate(row):
                if self.markers[col_val] == 'x':
                    row_marks += 1
                    col_marks[i] += 1
                    if col_marks[i] >= 5:
                        return True

            if row_marks >= 5:
                return True

        return False

    def makeDinner(self):
        for k, v in self.markers.items():
            if v != 'x':
                self.unmarked_sum += int(k)
        return self.unmarked_sum * int(self.last_marked)

    def setWinner(self):
        self.iWonAlready = True

    def toString(self):
        return self.tiles

def part1():
    '''part 1 of day 4'''

    gameboards = []
    num_re = re.compile(r'([0-9]+)')
    temp_gameboard = []
    raw_gameboards = None

    with open(infile_path, 'r') as f:

        # first line is playing numbers followed by empty line
        play_nums = f.readline().split(',')
        _ = f.readline()

        # read in boards
        lines = f.readlines()

        raw_gameboards = ''.join(lines).split('\n\n')

    # set up gameboards
    for gb in raw_gameboards:

        temp_gameboard = []
        for row in gb.split('\n'):
            temp_gameboard.append(num_re.findall(row))

        gameboards.append(PuzzleBoard(temp_gameboard))

    for play in play_nums:
        for board in gameboards:
            board.markTile(play)
            if board.checkWinner():
                return board.makeDinner()

def part2():
    '''part 2 of day 4'''
    gameboards = []
    num_re = re.compile(r'([0-9]+)')
    temp_gameboard = []
    raw_gameboards = None
    losing_board_count = 0

    with open(infile_path, 'r') as f:

        # first line is playing numbers followed by empty line
        play_nums = f.readline().split(',')
        _ = f.readline()

        # read in boards
        lines = f.readlines()

        raw_gameboards = ''.join(lines).split('\n\n')

    # set up gameboards
    for gb in raw_gameboards:

        temp_gameboard = []
        for row in gb.split('\n'):
            temp_gameboard.append(num_re.findall(row))

        gameboards.append(PuzzleBoard(temp_gameboard))

    losing_board_count = len(gameboards)

    for play in play_nums:
        for board in gameboards:
            board.markTile(play)

            if board.checkWinner() and not board.iWonAlready:
                board.setWinner()
                losing_board_count -= 1

                if losing_board_count == 0:
                    return board.makeDinner()

if __name__ == "__main__":
    answer1 = part1()
    print('part 1 answer: {}'.format(answer1))
    answer2 = part2()
    print('part 2 answer: {}'.format(answer2))