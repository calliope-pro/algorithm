# ABC244-D
# swapは転倒数関連の可能性がある
# 3つ等しい、1つ等しい、1つも等しくないときを抽出的に考えたら分かる
import sys

rs = lambda: sys.stdin.readline().split()

s = ''.join(rs())
t = ''.join(rs())
cnt = 0
for s_, t_ in zip(s, t):
    if s_ == t_:
        cnt += 1
if cnt == 1:
    print('No')
else:
    print('Yes')
