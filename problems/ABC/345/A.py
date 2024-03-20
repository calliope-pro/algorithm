import sys

rr = lambda: sys.stdin.readline().rstrip()

s = rr()
if s.startswith('<') and s.endswith('>') and "="*(len(s)-2) == s[1:-1]:
    print('Yes')
else:
    print('No')
