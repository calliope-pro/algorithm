# ABC334-B
# l, rはどのkのエリアにあるのかそれぞれ計算すればいい
import sys

rm = lambda: map(int, sys.stdin.readline().split())

a, m, l, r = rm()
k_l = (l-a+m-1) // m
k_r = (r-a) // m
print(k_r - k_l + 1)
