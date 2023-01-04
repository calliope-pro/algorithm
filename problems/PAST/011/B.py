# PAST011-B
# most_commonは全て取得するので、sortのkeyをしっかりと指定する必要がある
import collections
import sys

rr = lambda: sys.stdin.readline().rstrip()

s = rr()
print(sorted(collections.Counter(s1+s2 for s1, s2 in zip(s, s[1:])).most_common(), key=lambda t: (-t[1], t[0]))[0][0])
