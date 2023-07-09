# ABC309-A
# a,bの関係性と例外の条件分岐
import sys

rm = lambda: map(int, sys.stdin.readline().split())

a, b = rm()
if b-a == 1 and b != 4 and b != 7:
    print('Yes')
else:
    print('No')
