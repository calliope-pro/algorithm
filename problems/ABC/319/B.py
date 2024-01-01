# ABC319-B
# 愚直に指示を実装。
import sys

ri = lambda: int(sys.stdin.readline())

n = ri()
ans = []
for i in range(n+1):
    for j in range(1, 10):
        if n%j == 0 and i%(n//j) == 0:
            ans.append(str(j))
            break
    else:
        ans.append('-')
print(''.join(ans))
