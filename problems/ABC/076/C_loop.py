import sys

rr = lambda: sys.stdin.readline().rstrip()

s = rr()
t = rr()
len_s = len(s)
len_t = len(t)
for i in range(len_s - len_t, -1, -1):
    for sc, tc in zip(s[i:i+len_t], t):
        if sc == '?' or tc == '?':
            continue
        if sc != tc:
            break
    else:
        print(s[:i].replace(*'?a') + t + s[i+len_t:].replace(*'?a'))
        exit()
print('UNRESTORABLE')
