# ABC303-C
# また微妙な問題文でイライラする
# アイテムが使われると、そこからは消える。これあるならもっとテストケース出してほしい
# プログラムは、単純にシミュレーションするだけ
import sys

rr = lambda: sys.stdin.readline().rstrip()
rm = lambda: map(int, sys.stdin.readline().split())

n, m, h, k = rm()
s = rr()
x, y = 0, 0
items = {tuple(rm()) for _ in range(m)}
for direction in s:
    if direction == 'R':
        x += 1
    elif direction == 'L':
        x -= 1
    elif direction == 'U':
        y += 1
    else:
        y -= 1
    h -= 1
    if (x, y) in items and h >= 0 and h < k:
        h = k
        items.remove((x, y))
    if h < 0:
        print('No')
        exit()
print('Yes')
