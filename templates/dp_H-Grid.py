'''
5 5
..#..
.....
#...#
.....
..#..
'''
import sys

rl = sys.stdin.readline

h, w = map(int, rl().split())

li = []
dh = [0, -1]
dw = [-1, 0]
dp = [[0] * w for _ in range(h)]
dp[0][0] = 1
for _ in range(h):
    li.append(rl().rstrip())
for i in range(h):
    for j in range(w):
        if li[i][j] == '#':
            continue
        a = 0
        for k in range(2):
            nh = i + dh[k]
            nw = j + dw[k]
            if nh < 0 or nw < 0:
                continue
            a += dp[nh][nw]
        if dp[i][j] == 0:
            dp[i][j] = a
print((dp[-1][-1]) % (10**9 + 7))
