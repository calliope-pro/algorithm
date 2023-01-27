# ABC286-D
# PyPy only
# dpでもできるが、xの制約が小さい -> 保持すべき支払える額の個数が高々10^4 -> 全て保持してみた
import sys

rm = lambda: map(int, sys.stdin.readline().split())

n, x = rm()
set_ = set([0])
for _ in range(n):
    a, b = rm()
    set_tmp = set()
    for v in set_:
        for i in range(1, b+1):
            tmp = v + a*i
            if tmp > x:
                break
            set_tmp.add(tmp)
    set_.update(set_tmp)
if x in set_:
    print('Yes')
else:
    print('No')
