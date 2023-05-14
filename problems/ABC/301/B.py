# ABC301-B
# rangeを使って展開すればいい
# 最後の数を出力し忘れないこと
import sys

ri = lambda: int(sys.stdin.readline())
rl = lambda: list(map(int, sys.stdin.readline().split()))

n = ri()
al = rl()
for i in range(n-1):
    if al[i] < al[i+1]:
        print(*range(al[i], al[i+1]), end=' ')
    else:
        print(*range(al[i], al[i+1], -1), end=' ')
print(al[-1])
