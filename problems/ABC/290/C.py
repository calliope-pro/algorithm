# ABC290-C
# 全探索はもちろん無理 -> 規則性を見つける
# 小さい順に数をとっていけるかどうかを考えればいい
# 残ってるならそれの最小値を超えることはない。すべて取れるなら、k<=nより、kが答えになる
import sys

rm = lambda: map(int, sys.stdin.readline().split())
rl = lambda: list(map(int, sys.stdin.readline().split()))

n, k = rm()
al = rl()
ans = set(range(k))
for av in al:
    ans.discard(av)
if len(ans) == 0:
    print(k)
else:
    print(min(ans))
