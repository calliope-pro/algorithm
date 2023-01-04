# PAST007-B
# 制限的に愚直でいい。pythonのrangeが使いやすい
import sys

rm = lambda: map(int, sys.stdin.readline().split())

a, b, c = rm()
for i in range(a, 0, -1):
    if i <= b*c:
        print(i/b)
        exit()
