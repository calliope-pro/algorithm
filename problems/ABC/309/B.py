# ABC309-B
# 上下以外は同じ処理するだけ
import sys

rr = lambda: sys.stdin.readline().rstrip()
ri = lambda: int(sys.stdin.readline())

n = ri()
m = [rr() for _ in range(n)]
print(m[1][0] + m[0][:-1])
for i in range(1, n-1):
    print(m[i+1][0] + m[i][1:-1] + m[i-1][-1])
print(m[-1][1:] + m[-2][-1])
