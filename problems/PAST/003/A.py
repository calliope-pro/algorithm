# PAST003-A
# 条件分岐の順序を上手く活用
import sys

rr = lambda: sys.stdin.readline().rstrip()

s = rr()
t = rr()
if s == t:
    print('same')
    exit()
if s.lower() == t.lower():
    print('case-insensitive')
else:
    print('different')
