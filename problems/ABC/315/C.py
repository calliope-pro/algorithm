# ABC315-C
# 一番美味しいものは選択する。もう一つは全探索でよい
import sys

ri = lambda: int(sys.stdin.readline())
rm = lambda: map(int, sys.stdin.readline().split())

n = ri()
sf = []
for _ in range(n):
    f, s = rm()
    sf.append((s, f))
sf.sort(reverse=True)
ans = 0
f = sf[0][1]
for s, f_ in sf[1:]:
    if f != f_:
        ans = max(s+sf[0][0], ans)
    else:
        ans = max(s//2+sf[0][0], ans)
print(ans)
