# ABC283-B
# ループと入力をしっかりと捉える
import sys

ri = lambda: int(sys.stdin.readline())
rl = lambda: list(map(int, sys.stdin.readline().split()))

n = ri()
a = rl()
q = ri()

for _ in range(q):
    query = rl()
    if query[0] == 1:
        k = query[1]
        x = query[2]
        a[k-1] = x
    else:
        k = query[1]
        print(a[k-1])
