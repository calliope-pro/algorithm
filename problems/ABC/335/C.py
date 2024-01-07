# ABC335-C
# 後隊は頭の跡をたどるだけだから、前隊の移動を逆順にたどればよい。
# まだ跡が追えない時は初期位置からのずれを出す
# dequeだとTLEになるので、listでやるために。。。。
import sys

rs = lambda: sys.stdin.readline().split()
rm = lambda: map(int, sys.stdin.readline().split())

n, q = rm()
d = [(1, 0)]
for _ in range(q):
    k, v = rs()
    if k == '1':
        if v == 'R':
            d.append((d[-1][0]+1, d[-1][1]))
        elif v == 'L':
            d.append((d[-1][0]-1, d[-1][1]))
        elif v == 'U':
            d.append((d[-1][0], d[-1][1]+1))
        else:
            d.append((d[-1][0], d[-1][1]-1))
    else:
        v = int(v)
        if v > len(d):
            print(v-len(d)+1, 0)
        else:
            print(*d[len(d)-v])

