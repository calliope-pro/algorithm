import sys

ri = lambda: int(sys.stdin.readline())
rl = lambda: list(map(int, sys.stdin.readline().split()))

n = ri()
a = rl()
li = list(range(1, n+1))
cnt_0 = 0
cnt_1 = 0
for i, av in enumerate(a):
    lii = li[i]
    if av == lii:
        cnt_0 += 1
    elif av == li[av-1] and lii == a[av-1]:
        cnt_1 += 1
print(cnt_1//2 + (cnt_0*(cnt_0-1))//2)
