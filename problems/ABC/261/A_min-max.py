import sys
rm = lambda: map(int, sys.stdin.readline().split())

l1, r1, l2, r2 = rm()
l = max(l1, l2)
r = min(r1, r2)
print(max(0, r - l))
