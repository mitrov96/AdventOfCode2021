inp = [line.strip() for line in open('input_files/input_day_9.txt', 'r')]


def pos(x, y):
    yield x + 1, y
    yield x - 1, y
    yield x, y - 1
    yield x, y + 1


def isLow(x, y):
    for (nx, ny) in pos(x, y):
        if 0 <= nx < len(inp) and 0 <= ny < len(inp[0]):
            if inp[x][y] >= inp[nx][ny]:
                return False
    return True


def findBasin(x, y):
    b = set()
    a = set()
    a.add((x, y))
    while len(a) > 0:
        wa = a.copy()
        for (x, y) in wa:
            a.remove((x, y))
            b.add((x, y))
            for (nx, ny) in pos(x, y):
                if 0 <= nx < len(inp) and 0 <= ny < len(inp[0]):
                    if inp[nx][ny] < '9' and not (nx, ny) in b:
                        a.add((nx, ny))

    return b


# part 1
s = 0
for x in range(0, len(inp)):
    for y in range(0, len(inp[0])):
        if isLow(x, y):
            s += 1 + int(inp[x][y])
print(s)

# part 2
s = 0
bl = []
for x in range(0, len(inp)):
    for y in range(0, len(inp[0])):
        if isLow(x, y):
            b = findBasin(x, y)
            bl.append(len(b))
            # print(x, y, len(b))
bl.sort(reverse=True)
print(bl[0] * bl[1] * bl[2])