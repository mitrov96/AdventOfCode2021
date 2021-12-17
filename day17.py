import re

inp = [line.strip() for line in open('input_files/input_day_17.txt', 'r')][0]

(x1, x2, y1, y2) = map(int, re.findall(r'-?\d+', inp))


def findHitxVeloc(vx):
    global x1, x2
    cx = 0
    for t in range(1, x2 + 1):
        cx += vx
        if x1 <= cx <= x2:
            yield t, vx
            if vx == 0:
                return
        if cx > x2:
            break
        if vx > 0:
            vx -= 1


def hityVeloc(vy, t, keepfalling):
    global y1, y2
    cy = 0
    highy = 0
    for it in range(t):
        cy += vy
        vy -= 1
        if vy == 0:
            highy = cy
    while cy >= y1:
        if y1 <= cy <= y2:
            yield cy, highy
        if not keepfalling:
            break
        cy += vy
        vy -= 1
        if vy == 0:
            highy = cy


maxh = 0
vs = set()
for vx in range(1, x2 + 1):
    for ht, hvx1 in findHitxVeloc(vx):
        for vy in range(-500, 500):
            for cy, highy in hityVeloc(vy, ht, hvx1 == 0):
                maxh = max(maxh, highy)
                vs.add((vx, vy))

print("maxh", maxh)
print("vslen", len(vs))