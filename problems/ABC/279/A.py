# ABC279-A
# vとwの個数をstr.count使うだけ
import sys

rr = lambda: sys.stdin.readline().rstrip()

s = rr()
print(s.count('w')*2 + s.count('v'))
