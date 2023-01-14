# ABC276-D
# 2と3とその他に素因数分解する
# その他の素因数が複数個あるとダメ
# 2と3の個数で最低値を考える
import sys

ri = lambda: int(sys.stdin.readline())
rl = lambda: list(map(int, sys.stdin.readline().split()))

n = ri()
al = rl()
twos = [0] * n
threes = [0] * n
others = set()
for i, av in enumerate(al):
    cnt_2 = 0
    while True:
        if av % 2 == 0:
            av //= 2
            cnt_2 += 1
        else:
            break
    twos[i] = cnt_2
    cnt_3 = 0
    while True:
        if av % 3 == 0:
            av //= 3
            cnt_3 += 1
        else:
            break
    threes[i] = cnt_3
    others.add(av)

if len(others) != 1:
    print(-1)
    exit()
print(sum(twos) - min(twos)*n + sum(threes) - min(threes)*n)
