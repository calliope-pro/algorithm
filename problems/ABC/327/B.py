# ABC327-B
# 高々20^20なので、全探索でいける
import sys

ri = lambda: int(sys.stdin.readline())

b = ri()
for i in range(1, 20):
    if i**i == b:
        print(i)
        exit()
print(-1)
