# 典型90-070
# 天才かもしれん。マンハッタン距離完璧に理解した
# マンハッタン距離なので、x, yを独立して考えていい
# マンハッタン距離が変動するという微分を考えれば、中央値にあるとき必ず最小のマンハッタン距離になる
import sys

ri = lambda: int(sys.stdin.readline())
rm = lambda: map(int, sys.stdin.readline().split())

n = ri()
x = []
y = []
for _ in range(n):
    x_, y_ = rm()
    x.append(x_)
    y.append(y_)
x.sort()
y.sort()
xb = x[n//2]
yb = y[n//2]
x_sum = sum(abs(xb-xv) for xv in x)
y_sum = sum(abs(yb-yv) for yv in y)
print(x_sum + y_sum)
