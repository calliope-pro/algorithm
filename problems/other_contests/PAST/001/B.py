# PAST001-B
# 単なるシミュレート
import sys

ri = lambda: int(sys.stdin.readline())

n = ri()
a = ri()
for _ in range(n-1):
    a_ = ri()
    if a_ > a:
        print(f'up {a_ - a}')
    elif a_ == a:
        print('stay')
    else:
        print(f'down {a - a_}')
    a = a_
