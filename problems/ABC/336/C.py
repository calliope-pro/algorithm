# ABC336-C
# 5進数で考える
import sys
import math

ri = lambda: int(sys.stdin.readline())

n = ri()
ans = []
for i in range(1, 10*10):
    ans.append(str([0, 2, 4, 6, 8][n % 5 - 1]))
    n = math.ceil(n/5)
    if n == 0:
        break
print(int(''.join(ans[::-1])))
