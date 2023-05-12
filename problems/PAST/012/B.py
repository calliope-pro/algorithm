# PAST012-B
# 制約がバカ大きいので、文字列の長さとして考える。
# そもそも割り算は怖いのでね。。
import sys

rr = lambda: sys.stdin.readline().rstrip()

n = rr()
print(n[:-2] if len(n) > 2 else 0)
