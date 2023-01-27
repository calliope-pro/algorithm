# ABC255-C
# 定数項の場合の条件分岐が必要
# 公差数列なので、計算から大体の近い順番を求められる。
# 公差が負の可能性があるため、計算しやすいように正規化する
# それの前後を判定してみる
# 全体の項数が決められているので、それの上界・下界を越しているパターン等を考える必要はある
import sys

rm = lambda: map(int, sys.stdin.readline().split())

x, a, d, n = rm()
if d == 0:
    print(abs(x-a))
    exit()
if d < 0:
    min_, max_ = a+(n-1)*d, a
    d *= -1
else:
    min_, max_ = a, a+(n-1)*d

x_ = x - min_
n_ = x_//d
ans = min(abs(x-min_), abs(x-max_))
if 0 <= n_+1 <= n:
    ans = min(abs(min_+n_*d - x), ans)
if 0 <= n_+2 <= n:
    ans = min(abs(min_+(n_+1)*d - x), ans)
print(ans)
