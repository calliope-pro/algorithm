# 典型90-058
# kがバカ多い -> 数学的に計算できる箇所があるはず
# 今回はループ検出すればいい
# ループまでは高々10**5 -> 重複してる箇所をカウンター使って検出すれば間に合う <-> 他はナイーブにシミュレートで間に合う
import sys
import collections

rm = lambda: map(int, sys.stdin.readline().split())

n, k = rm()
counter = collections.Counter([n])
cnt = 0
add_flag = False
loop = []
M = 10**5
for _ in range(k):
    di_sum = sum(int(c) for c in str(n))
    z = (n + di_sum) % M
    if add_flag:
        loop.append(z)
        if counter[z] == 2:
            k -= cnt + 1
            k %= len(loop)
            print(loop[k])
            exit()
    else:
        cnt += 1
    if counter[z] == 1:
        add_flag = True
    counter[z] += 1
    n = z
print(z)



