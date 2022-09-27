# PAST011-A
# 愚直にシミュレートする必要は無く、累計時間を考えればいい
import sys

rm = lambda: map(int, sys.stdin.readline().split())

x, a, b, c = rm()
t_rabbit = c + x/a
t_turtle = x/b
if t_rabbit < t_turtle:
    print('Hare')
elif t_rabbit == t_turtle:
    print('Tie')
else:
    print('Tortoise')
