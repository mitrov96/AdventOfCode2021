from functools import reduce

inp = [line.strip() for line in open('input_files/input_day_13.txt', 'r')]

p = set()
f = []
for l in inp:
    if len(l) == 0:
        continue
    if l[0] == 'f':
        (t, fs) = l.split('=')
        y = 0
        x = 0
        if 'y' in t:
            y = fs
        else:
            x = fs
        f.append((int(x), int(y)))
    else:
        (x, y) = l.split(',')
        p.add((int(x), int(y)))


def printm(lst, f):
    for line in lst:
        s = reduce(lambda x, y: x + f(y), line, "")
        print(s)


def printp(p):
    maxx = max(list(p), key=lambda x: x[0])[0]
    maxy = max(list(p), key=lambda x: x[1])[1]
    s = [[' '] * (maxx + 1) for i in range(maxy + 1)]
    for x, y in p:
        s[y][x] = '#'
    printm(s, lambda x: x)


np1 = None
for fx, fy in f:
    np = set()
    for (x, y) in p:
        if x <= fx or fx == 0:
            nx = x
        else:
            nx = fx - (x - fx)
        if y <= fy or fy == 0:
            ny = y
        else:
            ny = fy - (y - fy)
        np.add((nx, ny))
    p = np
    if np1 is None:
        np1 = len(np)

print(np1)
printp(p) #PZEHRAER