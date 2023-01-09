# ABC284-A
# スライス記法とかメソッドで手短に
import sys

rr = lambda: sys.stdin.readline().rstrip()
ri = lambda: int(sys.stdin.readline())

n = ri()
sl = [rr() for _ in range(n)]
for s in sl[::-1]:
    print(s)
