# ABC284-B
# sumとiterableを組み合わせて短く
import sys

ri = lambda: int(sys.stdin.readline())
rl = lambda: list(map(int, sys.stdin.readline().split()))

t = ri()
for _ in range(t):
    n = ri()
    al = rl()
    print(sum(av&1 for av in al))
