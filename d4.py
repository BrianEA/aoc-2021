# Day 4: 
# Part 1:
# Part 2:
# 
from collections import defaultdict
import sys
#import pandas as pd

with open('input4.txt','r') as f:
   data = f.read().strip().split('\n\n')


# test:
# data = """7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

# 22 13 17 11  0
#  8  2 23  4 24
# 21  9 14 16  7
#  6 10  3 18  5
#  1 12 20 15 19

#  3 15  0  2 22
#  9 18 13 17  5
# 19  8  7 25 23
# 20 11 10 24  4
# 14 21 16 12  6

# 14 21 17 24  4
# 10 16 15  9 19
# 18  8 23 26 20
# 22 11 13  6  5
#  2  0 12  3  7""".split('\n\n')

draws = [x for x in data[0].strip().split(',')]
boards = []
boardNums = []
for boardNum, boardInput in enumerate(data[1:]):
    boards.append([])
    boardNums.append([])
    for y, yval in enumerate(boardInput.split('\n')):
        boards[boardNum].append([])
        for xval in yval.split():
            boards[boardNum][y].append(xval)
            boardNums[boardNum].append(int(xval))


def checkMatchX(boardIndex):
    for x in range(5):
        if len([n for n in boards[boardIndex][x] if int(n) in calledNums]) == 5:
            return True
    return False

def checkMatchY(boardIndex):
    for x in range(5):
        vals = boardNums[boardIndex][x::5]
        if len([n for n in vals if n in calledNums]) == 5:
            return True
    return False

boardWins = defaultdict(int)

def processDrawsP1():
    global calledNums
    calledNums = []
    for draw, drawNum in enumerate(draws):
        calledNums.append(int(drawNum))
        if draw > 3:
            for boardIndex, board in enumerate(boardNums):
                if len([x for x in board if x in calledNums]) >= 5:
                    if checkMatchX(boardIndex) or checkMatchY(boardIndex):
                        return boardIndex

def processDrawsP2():
    global calledNums
    calledNums = []    
    for draw, drawNum in enumerate(draws):
        calledNums.append(int(drawNum))
        if draw > 3:
            for boardIndex, board in enumerate(boardNums):
                if len([x for x in board if x in calledNums]) >= 5:
                    if checkMatchX(boardIndex) or checkMatchY(boardIndex):
                        boardWins[boardIndex] += 1                    
                        if len(boardWins.keys()) == len(boards):
                            return boardIndex

winBoardIndex = processDrawsP1()
unmarkedNums = [x for x in boardNums[winBoardIndex] if x not in calledNums]

print('Part 1:', sum(unmarkedNums) * calledNums[~0])

lastWinBoardIndex = processDrawsP2()
unmarkedNums = [x for x in boardNums[lastWinBoardIndex] if x not in calledNums]
print('Part 2:', sum(unmarkedNums) * calledNums[~0])

