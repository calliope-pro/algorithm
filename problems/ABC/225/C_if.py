import sys

rm = lambda: map(int, sys.stdin.readline().split())
rl = lambda: list(map(int, sys.stdin.readline().split()))

n, m = rm()
b = []

for i in range(n):
    b_ = rl()
    if i == 0:
        if b_[-1]%7 != 0 and b_[-1]%7 - m < 0:
            print('No')
            exit()
        for k, l in zip(b_[:-1], b_[1:]):
            if l-k != 1:
                print('No')
                exit()
    else:
        for k, l in zip(b[-1], b_):
            if l-k != 7:
                print('No')
                exit()
    b.append(b_)
print('Yes')
