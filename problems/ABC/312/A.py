# ABC312A
# setを使うだけ
import sys

rr = lambda: sys.stdin.readline().rstrip()

s = rr()
if s in {'ACE', 'BDF', 'CEG', 'DFA', 'EGB', 'FAC', 'GBD'}:
    print('Yes')
else:
    print('No')
