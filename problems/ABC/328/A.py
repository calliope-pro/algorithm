# ABC328-A
# filterを内包表記で実装するだけ
import sys

rm = lambda: map(int, sys.stdin.readline().split())
rl = lambda: list(map(int, sys.stdin.readline().split()))

n, x = rm()
sl = rl()
print(sum([s for s in sl if s <= x]))
