"""
5
3
1 1 1 0 1
1 1 0 0 0
1 0 0 0 1
"""
import sys
rl = sys.stdin.readline

m = int(rl())
n = int(rl())
lis = []
for _ in range(n):
    lis.append(list(map(int, rl().split())))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def dfs(y, x, c):
    global my_max
    lis[y][x] = 0
    if my_max < c:
        my_max = c
    for dx1, dy1 in zip(dx, dy):
        nx = x + dx1
        ny = y + dy1
        if nx < 0 or ny < 0 or nx >= m or ny >= n:
            continue
        elif lis[ny][nx] == 1:
            dfs(ny, nx, c+1)
    lis[y][x] = 1

my_max = 1
for j, li in enumerate(lis):
    for i, v in enumerate(li):
        if v:
            dfs(j, i, 1)

print(my_max)