# Paiza-A053
# DFSを未探索の場所で行うだけ、その遷移の個数が答え
# あとは探索場所の色により条件分岐
import sys
import itertools

rsl = lambda: list(sys.stdin.readline().rstrip())
rm = lambda: map(int, sys.stdin.readline().split())

sys.setrecursionlimit(10000000)

h, w = rm()
cm = [rsl() for _ in range(h)]
passed = [[0] * w for _ in range(h)]
def dfs(x=0, y=0):
    if passed[x][y] == 1:
        return
    passed[x][y] = 1
    for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        if 0 <= x+dx < h and 0 <= y+dy < w:
            if cm[x][y] == cm[x+dx][y+dy]:
                dfs(x+dx, y+dy)

rgb = [0, 0, 0]
for i, j in itertools.product(range(0, h), range(0, w)):
    if passed[i][j] == 0:
        dfs(i, j)
        if cm[i][j] == 'R':
            rgb[0] += 1
        elif cm[i][j] == 'G':
            rgb[1] += 1
        else:
            rgb[2] += 1
print(*rgb)
