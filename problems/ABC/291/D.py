# ABC291-D
# dpですね。これは2変数だから楽だ
# mod2で余りを出すの忘れてた
import sys

ri = lambda: int(sys.stdin.readline())
rm = lambda: map(int, sys.stdin.readline().split())
mod2 = 998244353

n = ri()
a_prev, b_prev = rm()
cnt_a, cnt_b = 1, 1
for _ in range(n-1):
    a, b = rm()
    cnt_a_tmp = 0
    cnt_b_tmp = 0
    if a_prev != a:
        cnt_a_tmp += cnt_a
    if b_prev != a:
        cnt_a_tmp += cnt_b
    if a_prev != b:
        cnt_b_tmp += cnt_a
    if b_prev != b:
        cnt_b_tmp += cnt_b
    a_prev = a
    b_prev = b
    cnt_a = cnt_a_tmp % mod2
    cnt_b = cnt_b_tmp % mod2
print((cnt_a + cnt_b) % mod2)
