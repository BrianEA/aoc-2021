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

# pairing up each depth reading with the next depth reading value
totalIncreases = sum([1 for d1, d2 in zip(depths, depths[1:]) if int(d1) < int(d2)])
print('Part 1: ', totalIncreases)

# summing each depth reading with the next 2 depth reading values, at each position
window1 = [d1+d2+d3 for d1, d2, d3 in zip(depths, depths[1:], depths[2:])]
# the same, from 1 position advanced
window2 = [d1+d2+d3 for d1, d2, d3 in zip(depths[1:], depths[2:], depths[3:])]
totalIncreases = sum([1 for d1, d2 in zip(window1, window2) if int(d1) < int(d2)])
print('Part 2: ', totalIncreases)