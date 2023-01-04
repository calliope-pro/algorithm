# PAST007-A
# pythonのスライスが活躍する
import sys

rr = lambda: sys.stdin.readline().rstrip()

s = rr()
odd = sum(int(c) for c in s[:-1:2]) * 3
even = sum(int(c) for c in s[1::2])
if (odd + even) % 10 == int(s[-1]):
    print('Yes')
else:
    print('No')
