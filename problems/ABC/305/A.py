import sys

ri = lambda: int(sys.stdin.readline())

n = ri()
print(n + 5 - n%5 if n % 5 > 2 else n - n%5)
