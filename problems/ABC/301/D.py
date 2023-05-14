# ABC301-D
# 2^60になるので、全探索はダメ
# 集合Tの最小値がnを超えるか
# 貪欲的に、bitが立つかどうかを調べる
import sys

rr = lambda: sys.stdin.readline().rstrip()
ri = lambda: int(sys.stdin.readline())

s = rr()
n = ri()
lb = int(s.replace('?', '0'), base=2)
if lb > n:
    print(-1)
    exit()
len_s = len(s)
for i, c in enumerate(s):
    if c != '?':
        continue
    b = 1 << (len_s - 1 - i)
    if lb | b <= n:
        lb |= b
print(lb)
