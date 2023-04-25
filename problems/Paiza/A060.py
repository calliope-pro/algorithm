# Paiza-A060
# DFSの実装に手こずった。。。
# 一度探索済みならばそこから探索してもすべて行き止まりになってしまうので、道に戻す更新は必要ない
import collections
import sys

rsl = lambda: list(sys.stdin.readline().rstrip())
rm = lambda: map(int, sys.stdin.readline().split())

sys.setrecursionlimit(10000000)

h, w = rm()
sm = []
s_x, s_y = 0, 0
for i in range(h):
    s = rsl()
    sm.append(s)
    if 'S' in s:
        s_x = i
        s_y = s.index('S')

d = collections.deque()

def dfs(x, y):
    sm[x][y] = '#'
    for (dx, dy, c) in [(1, 0, 'D'), (0, 1, 'R'), (-1, 0, 'U'), (0, -1, 'L')]:
        if 0 <= dx+x < h and 0 <= dy+y < w:
            if sm[dx+x][dy+y] == 'G':
                d.append(c)
                return True
            if sm[dx+x][dy+y] == '.':
                d.append(c)
                if dfs(dx+x, dy+y):
                    return True
                d.pop()
    return False

dfs(s_x, s_y)
print(*d, sep="")
