# 典型90-028
# 初の2次元いもす法
# +/-させる場所がとても重要、始点・終点が共に+1になる(1次元でみたときに+と-の列をそれぞれ作成する必要があるため)
import sys
import collections

ri = lambda: int(sys.stdin.readline())
rm = lambda: map(int, sys.stdin.readline().split())

n = ri()
m = 1002
lm = [[0]*m for _ in range(m)]
for _ in range(n):
    lx, ly, rx, ry = rm()
    lm[lx][ly] += 1
    lm[rx][ry] += 1
    lm[lx][ry] -= 1
    lm[rx][ly] -= 1
for i in range(m-1):
    for j in range(m):
        lm[i+1][j] += lm[i][j]
counter = collections.Counter()
for i in range(m):
    for j in range(m-1):
        lm[i][j+1] += lm[i][j]
    counter.update(lm[i])
for i in range(1, n+1):
    print(counter[i])


