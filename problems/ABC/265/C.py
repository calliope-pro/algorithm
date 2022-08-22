# ABC265-C
# 循環しない場合は一方通行になるため、最大マス目分を探索すればいい
import sys

rsl = lambda: list(sys.stdin.readline().rstrip())
rm = lambda: map(int, sys.stdin.readline().split())

h, w = rm()
grid = [rsl() for _ in range(h)]
i, j = 0, 0
for _ in range(h*w):
    s = grid[i][j]
    if s == 'U':
        if i <= 0:
            print(i+1, j+1)
            exit()
        i -= 1
    if s == 'D':
        if i >= h-1:
            print(i+1, j+1)
            exit()
        i += 1
    if s == 'L':
        if j <= 0:
            print(i+1, j+1)
            exit()
        j -= 1
    if s == 'R':
        if j >= w-1:
            print(i+1, j+1)
            exit()
        j += 1
print(-1)
