# 典型90-034
# [left, right)区間でrightを増やすと、要素の種類数は増えるという単調性を使う
# 区間が被っている箇所に関しては同じ個数、再現性が保証されている。->尺取り法
# 尺取り法でleft, rightを管理して、right-leftの最大値を求めれば良い
# 端まで行った際のrightをしっかりと考える。インデックスを加算したり、break入れたりする。
import sys
import collections

rm = lambda: map(int, sys.stdin.readline().split())
rl = lambda: list(map(int, sys.stdin.readline().split()))

n, k = rm()
al = rl()
counter = collections.Counter()
ans = 0
right = 0
for left in range(n):
    for i in range(right, n):
        av = al[i]
        if len(counter) == k and counter[av] == 0:
            break
        counter[av] += 1
    else:
        ans = max(n - left, ans)
        break
    right = i
    ans = max(right - left, ans)
    if counter[al[left]] == 1:
        del counter[al[left]]
    else:
        counter[al[left]] -= 1
print(ans)
