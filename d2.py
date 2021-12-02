# Day 2: Dive! https://adventofcode.com/2021/day/2
# Part 1: What do you get if you multiply your final horizontal position by your final depth?   
# Part 2: [Same question, with differnet depth calculation]
# Note: if there were signiticantly move types I wouldn't use if/elif/elif, 
#   I'd probably leverage a combination of map and elements of the operator module

lines = open('input2.txt','r').readlines()

#test:
# lines = """forward 5
# down 5
# forward 8
# bop 3
# down 8
# forward 2""".splitlines()

horz = 0
depth = 0

for line in lines:
    move, dx = line.split()
    dx = int(dx)
    if move == 'forward':
        horz += dx
    elif move == 'down':
        depth += dx
    elif move == 'up':
        depth -= dx
    else:
        raise Exception('Unexpected move: ' + move)
     
print('Part 1: ', horz*depth)

# can retain final horizontal position value from part 1 for final expression
depth = 0
aim = 0

for line in lines:
    move, dx = line.split()

    dx = int(dx)
    if move == 'forward':
        depth += aim * dx
    elif move == 'down':
        aim += dx
    elif move == 'up':
        aim -= dx        
    else:
        raise Exception('Unexpected move: ' + move)

print('Part 2: ', horz*depth)