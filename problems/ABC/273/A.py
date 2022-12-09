# ABC273-A
# 再帰関数で階乗を求めた(math.factorialでも良い -> https://atcoder.jp/contests/abc273/submissions/37110332)
import sys

ri = lambda: int(sys.stdin.readline())

n = ri()
def f(k):
    if k == 0:
        return 1
    return f(k-1) * k
print(f(n))
