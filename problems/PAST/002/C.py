# PAST002-B
# インデックスをしっかりと管理してシミュレーションするだけ
import sys

rsl = lambda: list(sys.stdin.readline().rstrip())
ri = lambda: int(sys.stdin.readline())

n = ri()
s = [rsl() for _ in range(n)]
for i in range(n-2, -1, -1):
    for j in range(1, 2*n-2):
        if s[i][j] == '#' and 'X' in s[i+1][j-1]+s[i+1][j]+s[i+1][j+1]:
            s[i][j] = 'X'
for sl in s:
    print(''.join(sl))
