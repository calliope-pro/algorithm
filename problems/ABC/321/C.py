# ABC321-C
# めんどくさいですね〜
# 桁数の制御と、合計値の制御を再帰的にがんばる
import sys

ri = lambda: int(sys.stdin.readline())

k = ri()
ans = []


def f(base, prev, d):
    if d == 1:
        ans.extend([base * 10 + i for i in range(prev)])
        return
    for i in range(d - 1, prev):
        f(base * 10 + i, i, d - 1)


for i in range(1, 11):
    f(0, 10, i)
print(ans[k])
