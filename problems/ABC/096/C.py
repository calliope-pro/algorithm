# ABC096-C
# 愚直に全探索、上下左右に'#'が存在するか判定
import sys

rr = lambda: sys.stdin.readline().rstrip()
rm = lambda: map(int, sys.stdin.readline().split())

h, w = rm()
s = [rr() for _ in range(h)]
for i in range(h):
    for j in range(w):
        if s[i][j] == '#':
            didj = ((1, 0), (0, 1), (-1, 0), (0, -1))
            for di, dj in didj:
                if 0 <= i + di < h and 0 <= j + dj < w:
                    if s[i + di][j + dj] == '#':
                        break
            else:
                print('No')
                exit()
print('Yes')
