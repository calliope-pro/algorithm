# ABC349-B
# 文字の出現回数から、ある回数出現文字のリストを作成し、そのリストの長さが0か2ならYes、それ以外ならNo
import collections
import sys

rr = lambda: sys.stdin.readline().rstrip()

s = rr()
c = collections.Counter(s)
d = collections.defaultdict(list)
for k, cnt in c.items():
    d[cnt].append(k)

for k, v in d.items():
    if len(d[k]) == 0 or len(d[k]) == 2:
        continue
    else:
        print("No")
        exit()
print("Yes")
