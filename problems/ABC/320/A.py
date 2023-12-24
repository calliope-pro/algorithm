# ABC320-A
# 書いてあるとおりに実装するだけ
import sys

rm = lambda: map(int, sys.stdin.readline().split())

a, b = rm()
print(a**b + b**a)
