# ABC303-A
# 違うときに抜けるループ、条件分岐だるいので、ソートした文字列があるか否か見た
import sys

rr = lambda: sys.stdin.readline().rstrip()
ri = lambda: int(sys.stdin.readline())

n = ri()
s = rr()
t = rr()
for s_, t_ in zip(s, t):
    if s_ != t_:
        c = ''.join(sorted([s_, t_]))
        if c not in ['1l', '0o']:
            print('No')
            exit()
print('Yes')
