# ABC245-C
# dpと同じ。制約緩いためset使って強引に計算量を減らした
import sys

rm = lambda: map(int, sys.stdin.readline().split())
rl = lambda: list(map(int, sys.stdin.readline().split()))

n, k = rm()
a =  rl()
b = rl()
tmp = set([a[0], b[0]])
for a_, b_ in zip(a[1:], b[1:]):
    set_ = set()
    for i in tmp:
        if abs(i - a_) <= k:
            set_.add(a_)
        if abs(i - b_) <= k:
            set_.add(b_)
    if len(set_) == 0:
        print('No')
        exit()
    tmp = set_
print('Yes')
