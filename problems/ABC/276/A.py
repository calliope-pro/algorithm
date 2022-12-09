# ABC276-A
# str.rfindがただただ楽
import sys

rr = lambda: sys.stdin.readline().rstrip()

s = rr().rfind('a')
print(s + 1 if s != -1 else -1)
