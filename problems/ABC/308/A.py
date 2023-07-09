# ABC308-A
# すべての要素に対してのboolなので、all関数使うだけ
import sys

rl = lambda: list(map(int, sys.stdin.readline().split()))

sl = rl()
for a, b in zip(sl, sorted(sl)):
    if a != b:
        print('No')
        exit()
if all(100<=a<=675 and a%25==0 for a in sl):
    print('Yes')
else:
    print('No')
