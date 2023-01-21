# ABC252-C
# Cにしてはだるい、スロットの順番を変えていいのがクソ条件
# 各々の数字が出てくる箇所を辞書で保存しておくといい
import sys
import collections

rr = lambda: sys.stdin.readline().rstrip()
ri = lambda: int(sys.stdin.readline())
inf = float('inf')

n = ri()
d = collections.defaultdict(lambda: [])
for _ in range(n):
    s_ = rr()
    for i, c in enumerate(s_):
        d[c].append(i)

ans = inf
for key, val in d.items():
    counter = collections.Counter(val)
    tmp = set()
    for idx, cnt in sorted(counter.items()):
        for j in range(cnt):
            tmp.add(idx + j*10)
    ans = min(max(tmp), ans)
print(ans)
