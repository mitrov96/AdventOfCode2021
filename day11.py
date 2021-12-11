inp = [line.strip() for line in open('input_files/input_day_11.txt', 'r')]


def pos(x, y):
    for nx, ny in [(x + 1, y), (x - 1, y), (x, y - 1), (x, y + 1),
                   (x + 1, y + 1), (x + 1, y - 1), (x - 1, y + 1), (x - 1, y - 1)]:
        if 0 <= nx < H and 0 <= ny < W:
            yield nx, ny


(H, W) = (len(inp), len(inp[0]))
e = list(map(lambda x: list(map(int, x)), inp))
cnt = 0
r = 0

while True:
    r += 1
    for x in range(H):
        for y in range(W):
            e[x][y] += 1

    flashes = set()
    while True:
        found = False
        for x in range(H):
            for y in range(W):
                if e[x][y] > 9:
                    if not (x, y) in flashes:
                        flashes.add((x, y))
                        found = True
                        for (nx, ny) in pos(x, y):
                            e[nx][ny] += 1
        if not found:
            break

    for (x, y) in flashes:
        e[x][y] = 0

    cnt += len(flashes)

    if r == 100:
        print("sln1", cnt)

    if len(flashes) == H * W:
        print("sln2", r)
        break
