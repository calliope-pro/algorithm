import sys

rr = lambda: sys.stdin.readline().rstrip()
rm = lambda: map(int, sys.stdin.readline().split())

h, w = rm()
sample = None
for i in range(h):
    s = rr()
    if '#' in s:
        if sample is None:
            sample = (s, i)
        elif sample[0].count('#') > s.count('#'):
            for j in range(w):
                if s[j] != sample[0][j]:
                    print(i+1, j+1)
                    exit()
        elif sample[0].count('#') < s.count('#'):
            for j in range(w):
                if s[j] != sample[0][j]:
                    print(sample[-1]+1, j+1)
                    exit()
