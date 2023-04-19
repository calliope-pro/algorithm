# 典型90-085
# PyPy only
# a <= b <= cなので、aの上限がkの3乗根とわかる。aが定数条件下では、b <= cのk=k//cの2変数になるだけ
# 計算量はルートで判定になるので、ループさせるだけ
import sys

ri = lambda: int(sys.stdin.readline())

k = ri()
cnt = 0
for a in range(1, 10**4+1):
    if a ** 3 > k:
        break
    if k % a == 0:
        max_b = k // a
        for b in range(a, max_b + 1):
            if b ** 2 > max_b:
                break
            if max_b % b == 0:
                c = max_b // b
                if b <= c:
                    cnt += 1
print(cnt)
