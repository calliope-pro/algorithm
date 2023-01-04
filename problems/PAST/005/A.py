# PAST005-A
# 普通に`in`を使う
import sys

rr = lambda: sys.stdin.readline().rstrip()

s = rr()
if 'ooo' in s:
    print('o')
elif 'xxx' in s:
    print('x')
else:
    print('draw')
