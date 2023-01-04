# ABC283-C
# 制約が大きいので、数学的ではなく文字列的に処理
import sys

rr = lambda: sys.stdin.readline().rstrip()

s = rr()
print(len(s) - s.count('00'))
