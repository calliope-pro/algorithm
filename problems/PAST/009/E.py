# PAST009-E
# 条件通りにシミュレーションするだけ
import sys

rr = lambda: sys.stdin.readline().rstrip()

n = rr()
previousKey = n[0]
ans = 500
left_set = {'1', '2', '3', '4', '5'}
for c in n[1:]:
    if c == previousKey:
        ans += 301
    elif (previousKey in left_set) == (c in left_set):
        ans += 210
        previousKey = c
    else:
        ans += 100
        previousKey = c
print(ans)
