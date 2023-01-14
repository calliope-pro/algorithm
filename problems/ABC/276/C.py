# ABC276-C
# 規則性を見抜く
# 制約はそこまで厳しくないので、リストをゴリゴリ使おう
import sys

ri = lambda: int(sys.stdin.readline())
rl = lambda: list(map(int, sys.stdin.readline().split()))

n = ri()
pl = rl()
for i in range(n-1, -1, -1):
    if pl[i] < pl[i-1]:
        max_ = 0
        for j in pl[i:]:
            if j < pl[i-1]:
                max_ = max(j, max_)
        tmp = pl[i:]
        tmp.remove(max_)
        pl = pl[:i-1] + [max_] + sorted(tmp + [pl[i-1]], reverse=True)
        print(*pl)
        break
