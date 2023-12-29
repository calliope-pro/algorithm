import sys

rm = lambda: map(int, sys.stdin.readline().split())

b, g = rm()
if b < g:
    print('Glove')
else:
    print('Bat')
