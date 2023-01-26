# ABC092-C
# 制約的に2重ループは出来ない
# 差に着目するといい。差に関して事前計算しておくことで計算量を減らせる
import sys

ri = lambda: int(sys.stdin.readline())
rl = lambda: list(map(int, sys.stdin.readline().split()))

n = ri()
al = [0] + rl() + [0]
diff = [abs(a-b) for a, b in zip(al, al[1:])]
sum_ = sum(diff)
diff1 = [a+b for a, b in zip(diff, diff[1:])]
diff2 = [abs(a-b) for a, b in zip(al, al[2:])]
for diff1_, diff2_ in zip(diff1, diff2):
    print(sum_ - (diff1_ - diff2_))
