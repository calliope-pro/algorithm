# 典型90-010
# 累積和と複数リストを使う
import sys

ri = lambda: int(sys.stdin.readline())
rm = lambda: map(int, sys.stdin.readline().split())

n = ri()
sum_1 = [0]
sum_2 = [0]
for _ in range(n):
    c, p = rm()
    if c == 1:
        sum_1.append(sum_1[-1] + p)
        sum_2.append(sum_2[-1])
    else:
        sum_1.append(sum_1[-1])
        sum_2.append(sum_2[-1] + p)
q = ri()
for _ in range(q):
    l, r = rm()
    print(sum_1[r] - sum_1[l-1], sum_2[r] - sum_2[l-1])
