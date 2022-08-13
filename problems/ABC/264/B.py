# ABC264-B
# チェビシェフ距離を出せると差がつくし速い
import sys

rm = lambda: map(int, sys.stdin.readline().split())

r, c = rm()

# 愚直にシミュレートしてから算出
def f():
    grid = [None] * 15
    for i in range(8):
        i_ = i//2
        if i % 2 == 0:
            li = ['black', 'white'] * i_ + ['black'] * (15 - i_*4) + ['white', 'black'] * i_
        else:
            li = ['black'] + ['white', 'black'] * i_ + ['white'] * (13 - i_*4) + ['white', 'black'] * i_ + ['black']
        grid[i] = li
        grid[14-i] = li
    print(grid[r-1][c-1])

# 中心からのチェビシェフ距離を用いる
def f():
    dist = max(abs(r - 8), abs(c - 8))
    if dist & 1:
        print('black')
    else:
        print('white')

f()
