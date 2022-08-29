# PAST006-B
# aとoしか差が無い->p,s,tを削除してindex特定することで楽に
import sys

rr = lambda: sys.stdin.readline().rstrip()

s = rr()
s = s.replace('p', '').replace('s', '').replace('t', '')
if 'o' in s:
    print(s.index('o')+1)
else:
    print('none')

