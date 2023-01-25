# ABC254-C
# k飛ばしのときにそれぞれの組で同じ要素であるか判定すればいい。
import sys

rm = lambda: map(int, sys.stdin.readline().split())
rl = lambda: list(map(int, sys.stdin.readline().split()))

n, k = rm()
al = rl()
sorted_al = sorted(al)
if k == 1:
    print('Yes')
    exit()
for i in range(k):
    if sorted(al[i::k]) != sorted_al[i::k]:
        print('No')
        exit()
print('Yes')
