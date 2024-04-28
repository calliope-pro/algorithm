# ABC349-C
# 文字列Sの3文字がTの部分文字列になるかを判定する
# Tの最後がXの場合は2文字で判定する
import sys

rr = lambda: sys.stdin.readline().rstrip()

s = rr()
t = rr()
i = 0
for c in s:
    if c.upper() == t[i]:
        i += 1
    if i == 3:
        print("Yes")
        exit()
if i == 2 and t[-1] == "X":
    print("Yes")
    exit()
print("No")
