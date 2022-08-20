# ARC164-A
# 列挙をなるべく減らす工夫として事前にソート
import sys

rs = lambda: sys.stdin.readline().split()
ri = lambda: int(sys.stdin.readline())

n = ri()
a = rs()
a.sort(reverse=True, key=lambda x: (len(x), x))
ans = 0
ans = max(int(a[0] + a[1] + a[2]), ans)
ans = max(int(a[0] + a[2] + a[1]), ans)
ans = max(int(a[1] + a[0] + a[2]), ans)
ans = max(int(a[1] + a[2] + a[0]), ans)
ans = max(int(a[2] + a[1] + a[0]), ans)
ans = max(int(a[2] + a[0] + a[1]), ans)
print(ans)
