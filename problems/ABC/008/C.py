# ABC008-C
# 良問や。。
# 合計 / 場合の数 = それぞれでの期待値の総和と読み替える
# 表裏になるパターンを考える -> 約数の個数の偶奇性
# 順列なので、全ての場所での確率が等しい。 -> 約数が計何個あるか考えるだけでいい
import sys

ri = lambda: int(sys.stdin.readline())

n = ri()
cl = [ri() for _ in range(n)]
ans = 0
for v in cl:
    cnt = -1
    for factor in cl:
        if v % factor == 0:
            cnt += 1
    if cnt & 1:
        ans += 0.5
    else:
        ans += (cnt + 2) / (2*cnt + 2)
print(ans)
