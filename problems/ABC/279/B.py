# ABC279-B
# 文字列が包含されているかinを使うだけ
import sys

rr = lambda: sys.stdin.readline().rstrip()

s = rr()
t = rr()
print('Yes' if t in s else 'No')
