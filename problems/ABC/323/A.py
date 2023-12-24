# ABC323 - A
# rangeをうまく使うだけ
import sys

rr = lambda: sys.stdin.readline().rstrip()

s = rr()
for c in s[1::2]:
    if c == '1':
        print('No')
        exit()
print('Yes')
