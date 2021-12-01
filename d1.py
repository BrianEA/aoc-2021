# Day 1: Sonar Sweep
# Part 1: Count number of cases where a value in input is higher than the previous value
# Part 2: Viewing three values at a time (window), compare with previous 3 value window,
#  counting cases where sum of window values is more than the prior window sum.
depths = [int(x) for x in open('input1.txt','r').readlines()]

## test:
# depths = """199
# 200
# 208
# 210
# 200
# 207
# 240
# 269
# 260
# 263""".splitlines()
# depths = [int(x) for x in depths]


def sumIncreases(list1, list2):
    return sum(d1 < d2 for d1, d2 in zip(list1, list2))

print('Part 1: ', sumIncreases(depths, depths[1:]))

window1 = [d1+d2+d3 for d1, d2, d3 in zip(depths, depths[1:], depths[2:])]
window2 = [d1+d2+d3 for d1, d2, d3 in zip(depths[1:], depths[2:], depths[3:])]

print('Part 2: ', sumIncreases(window1, window2))