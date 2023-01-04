# PAST007-C
# コーナーケースに注意
import sys

rr = lambda: sys.stdin.readline().rstrip()
rm = lambda: map(int, sys.stdin.readline().split())

s = rr()
l, r = rm()
if (s == '0' or s[0] != '0') and l <= int(s) <= r:
    print('Yes')
else:
    print('No')
