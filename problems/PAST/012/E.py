# PAST012-E
# クソ問
# 問題の文章がゴミすぎ。意味わからんし、例も分かりにくすぎる。なんなんこれ。。。
# 前から単純にシミュレート。あとは条件分岐するだけ
import sys

rm = lambda: map(int, sys.stdin.readline().split())
rl = lambda: list(map(int, sys.stdin.readline().split()))

r, n, m, l = rm()
sl = rl()
cnt = 0
sum_tmp = 0
r_cnt = 0
for sv in sl:
    cnt += 1
    if sum_tmp + sv > n:
        print('No')
        exit()
    elif sum_tmp + sv == n or cnt == m:
        r_cnt += 1
        cnt = 0
        sum_tmp = 0
    else:
        sum_tmp += sv
else:
    if 0 < sum_tmp < n or 0 < cnt < m:
        print('No')
        exit()
print('YNeos'[r_cnt!=r::2])
