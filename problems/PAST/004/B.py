# PAST004-B
# 切り捨て除算と余りを上手く扱うことで対応
# formatの指定に気を付ける
import sys

rm = lambda: map(int, sys.stdin.readline().split())

x, y = rm()
if y == 0:
    print('ERROR')
    exit()
print(f'{x//y}.{(x*100//y)%100:02d}')
