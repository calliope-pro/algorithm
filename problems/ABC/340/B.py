# ABC340-B
# list使うだけ
import sys

ri = lambda: int(sys.stdin.readline())
rm = lambda: map(int, sys.stdin.readline().split())

tmp = []
q = ri()
for _ in range(q):
    i, v = rm()
    if i == 1:
        tmp.append(v)
    else:
        print(tmp[-v])
