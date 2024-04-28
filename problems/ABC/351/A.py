# ABC351-A
# sumして引くだけ
import sys

rl = lambda: list(map(int, sys.stdin.readline().split()))

al = rl()
bl = rl()
print(max(0, sum(al) - sum(bl) + 1))
