# ABC273-C
# セットと辞書を使い計算量を落とす
import sys

ri = lambda: int(sys.stdin.readline())
rl = lambda: list(map(int, sys.stdin.readline().split()))

n = ri()
a = rl()
s = set(a)
l = len(s)
c = {sv: l-i-1 for i, sv in enumerate(sorted(s))}
ans = [0]*n
for av in a:
    ans[c[av]] += 1
print(*ans, sep='\n')
