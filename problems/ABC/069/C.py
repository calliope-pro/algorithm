# ABC069-C
# 4の倍数、2の倍数、奇数で個数を分けて考えて
# [奇数, 4の倍数, ...]が最適、2の倍数と4の倍数だけなら問題ない
# [..., 4の倍数, 奇数]とか、[..., 奇数, 2の倍数]とかをきちんと考えてコーナーケースを対処する
import sys

ri = lambda: int(sys.stdin.readline())
rl = lambda: list(map(int, sys.stdin.readline().split()))

n = ri()
al = rl()
li024 = [0] * 3
for av in al:
    if av % 4 == 0:
        li024[2] += 1
    elif av % 2 == 0:
        li024[1] += 1
    else:
        li024[0] += 1

if li024[0] > li024[2] + 1:
    print('No')
    exit()

if li024[0] - li024[2] > 0 and li024[1]:
    print('No')
    exit()
print('Yes')
