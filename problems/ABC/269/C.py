# ABC269-C
# 1のフラグが立ってる箇所は15個しかない -> 高々答えは2^15個
# 要素をフラグごとに全て更新しても間に合う
import sys

ri = lambda: int(sys.stdin.readline())

n = bin(ri())[2:][::-1]
set_ = set([0])
for i, c in enumerate(n):
    if c == '1':
        set_tmp = set()
        for v in set_:
            set_tmp.add(v + 2**i)
        set_.update(set_tmp)
print(*sorted(set_), sep='\n')
