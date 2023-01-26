# ABC101-C
# 1~Nの並びかえたリスト -> 最小値は必ず1
# n個の要素から1つ以上の要素が被るようにk個の区間を取るようにすればいい。
# これの下界を求めれば答えになる
import sys
import math

rm = lambda: map(int, sys.stdin.readline().split())
rl = lambda: list(map(int, sys.stdin.readline().split()))

n, k = rm()
al = rl()
ans = math.ceil((n-1) / (k-1))
print(ans)
