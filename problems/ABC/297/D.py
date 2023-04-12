# ABC297-D
# どれくらい引くことができるかを計算すれば、割り算するだけだから計算量自体はそんなにかからない。
# math.ceilだと浮動小数点数によるずれが生じるので注意。。。。
import sys

rm = lambda: map(int, sys.stdin.readline().split())

a, b = rm()
ans = 0
while a != b:
    if b < a:
        a, b = b, a
    cnt = -(-b // a) - 1
    a, b = b-cnt*a, a
    ans += cnt
print(ans)
