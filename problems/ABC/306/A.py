# ABC306-A
# Pythonの内包表記最強です
import sys

rr = lambda: sys.stdin.readline().rstrip()
ri = lambda: int(sys.stdin.readline())

n = ri()
s = rr()
print(''.join(c*2 for c in s))
