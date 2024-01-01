# ABC318-B
# すべて0の二次元配列を作っておいて、シートがあるところを1にする
import sys

ri = lambda: int(sys.stdin.readline())
rm = lambda: map(int, sys.stdin.readline().split())

n = ri()
map_ = [[0]*100 for _ in range(100)]
for _ in range(n):
    a, b, c, d = rm()
    for i in range(a, b):
        for j in range(c, d):
            map_[i][j] = 1
print(sum(map(sum, map_)))
