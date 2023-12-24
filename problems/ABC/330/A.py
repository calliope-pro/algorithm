# ABC330-A
# filterを内包表記で実装するだけ
import sys

rm = lambda: map(int, sys.stdin.readline().split())
rl = lambda: list(map(int, sys.stdin.readline().split()))

n, l = rm()
al = rl()
print(len([a for a in al if a >= l]))
