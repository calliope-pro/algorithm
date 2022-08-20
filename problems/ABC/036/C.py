# ABC036-C
# 座圧するだけ
import sys

ri = lambda: int(sys.stdin.readline())

n = ri()
a = [ri() for _ in range(n)]
d = {sv: i for i, sv in enumerate(sorted(set(a)))}
print(*map(lambda v: d[v], a), sep='\n')
