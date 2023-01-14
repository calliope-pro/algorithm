# PAST007-E
# 制約小さいのできちんとシミュレーションするだけ
import sys

ri = lambda: int(sys.stdin.readline())

n = ri()
for i in range(30):
    x = 1
    for j in range(30):
        x *= 3
        if j == i:
            x += 1
    if x == n:
        print(i+1)
        exit()
print(-1)
