import re
from collections import defaultdict

inp = [line.strip() for line in open('input_files/input_day_6.txt', 'r')]
fish = list(map(int, re.findall(r'\d+', inp[0])))


def Solve(rounds):
    d = defaultdict(int)
    for f in fish:
        d[f] += 1
    for r in range(0, rounds):
        zeros = d[0]
        for i in range(1, 8 + 1):
            d[i - 1] = d[i]
        d[6] += zeros
        d[8] = zeros

    l = sum(d.values())
    print(l)


Solve(80)
Solve(256)