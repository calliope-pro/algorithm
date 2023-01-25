# ABC237-D
# 良い面白い問題
# dequeが使えるように見えるが、実直な実装だと出来ない -> 逆順だと出来る
# 逆転の発想！！
import sys
import collections

rr = lambda: sys.stdin.readline().rstrip()
ri = lambda: int(sys.stdin.readline())

n = ri()
s = rr()
d = collections.deque([n])
for i, c in enumerate(s[::-1], 1):
    if c == 'R':
        d.appendleft(n-i)
    else:
        d.append(n-i)
print(*d)
