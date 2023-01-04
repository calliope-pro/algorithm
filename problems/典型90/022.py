# 典型90-022
# 最大公約数を取得して、切る回数を求める
import sys
import math

rm = lambda: map(int, sys.stdin.readline().split())

a, b, c = rm()
gcd_ = math.gcd(math.gcd(a, b), c)
print(a//gcd_ + b//gcd_ + c//gcd_ - 3)
