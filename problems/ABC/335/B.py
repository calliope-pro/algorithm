# ABC335-B
# 脳死で3重ループで全探索
import sys

ri = lambda: int(sys.stdin.readline())

n = ri()
for x in range(22):
    for y in range(22):
        for z in range(22):
            if x + y + z <= n:
                print(x, y, z)
