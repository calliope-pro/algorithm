# ABC304-A
# Aにしてはむずかしいだろ。。。
# minになるやつ探してそこからスライス使ってループ
import sys

rs = lambda: sys.stdin.readline().split()
ri = lambda: int(sys.stdin.readline())

n = ri()
sa = [rs() for _ in range(n)]
min_v = min(sa, key=lambda x: int(x[1]))
min_idx = sa.index(min_v)
print(*[s for s, _ in sa[min_idx:]+sa[:min_idx]], sep='\n')
