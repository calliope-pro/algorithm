# ABC340-A
# rangeって便利、シーケンス型だからね
import sys

rm = lambda: map(int, sys.stdin.readline().split())

a, b, d = rm()
print(*range(a, b+1, d))
