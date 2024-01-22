# ABC035-B
# 有効となる向きの回数を数える、最後に?の数を考慮する
# 最大値は簡単、最小値は?の数とすでに移動した距離を考慮する
import sys
import collections

rr = lambda: sys.stdin.readline().rstrip()
ri = lambda: int(sys.stdin.readline())

c = collections.Counter(rr())
y = abs(c['U'] - c['D'])
x = abs(c['L'] - c['R'])
t = ri()
cq = c['?']
if t == 1:
    print(y + x + cq)
else:
    if cq < x+y:
        print(x+y-cq)
    else:
        if (x+y-cq) & 1:
            print(1)
        else:
            print(0)
