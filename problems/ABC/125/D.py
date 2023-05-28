# ABC125-D
# DはdpのD!
# 初期状態と遷移を渡して実装。最後は前の状態から計算する
import sys

ri = lambda: int(sys.stdin.readline())
rl = lambda: list(map(int, sys.stdin.readline().split()))

n = ri()
al = rl()
ans = [al[0], -al[0]]
for av in al[1:-1]:
    ans = [max(ans[0]+av, ans[1]-av), max(ans[1]+av, ans[0]-av)]
print(max(ans[0]+al[-1], ans[1]-al[-1]))
