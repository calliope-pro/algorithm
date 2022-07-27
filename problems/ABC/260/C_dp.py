import sys

rm = lambda: map(int, sys.stdin.readline().split())

n, x, y = rm()

red = 1
blue = 0
while n > 1:
    blue += red * x
    red += blue
    blue *= y
    n -= 1
print(blue)
