# ABC271-C
# 重複した巻は絶対使われない
# その次に大きい巻が使われない
# 前から貪欲に巻が存在しているか判定し、存在していないなら後ろの使われない巻を2つで代用
import sys
import collections

ri = lambda: int(sys.stdin.readline())
rl = lambda: list(map(int, sys.stdin.readline().split()))

n = ri()
al = rl()
c = collections.Counter(al)
al = list(c.keys())
al.sort()
for key, value in c.items():
    if value >= 2:
        al.extend([key] * (value-1))
d = collections.deque(al)
cnt = 0
while len(d):
    dv = d[0]
    try:
        if dv != cnt+1:
            d.pop()
            d.pop()
        else:
            d.popleft()
    except:
        break
    cnt += 1
print(cnt)
