# ABC338-B
# Counter使って、sort使ったら楽
import collections
import sys

rr = lambda: sys.stdin.readline().rstrip()

c = collections.Counter(rr())
print(sorted(c.most_common(30), key=lambda x: (-x[1], x[0]))[0][0])
