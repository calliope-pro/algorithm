# ABC347-B
# 短いので愚直に数え上げる
import sys

rr = lambda: sys.stdin.readline().rstrip()

s = rr()
ans = set()
for i in range(len(s)):
    for j in range(i, len(s)):
        ans.add(s[i:j+1])
print(len(ans))
