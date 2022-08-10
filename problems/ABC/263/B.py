# ABC263-B
# DFSと変わらないただのループ
import sys

ri = lambda: int(sys.stdin.readline())
rl = lambda: list(map(int, sys.stdin.readline().split()))

n = ri()
p = rl()
p.reverse()
ans = 1
ancestor = p[0]
while True:
    if ancestor == 1:
        print(ans)
        exit()
    ancestor = p[-ancestor+1]
    ans += 1
