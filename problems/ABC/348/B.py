# ABC348-B
# 単純に全探索するだけ同じ点のときcontinueするのは忘れない
import sys

ri = lambda: int(sys.stdin.readline())
rl = lambda: list(map(int, sys.stdin.readline().split()))

n = ri()
xy = [(i + 1, *rl()) for i in range(n)]
for i, x1, y1 in xy:
    max_ = 0
    ans = 0
    for j, x2, y2 in xy:
        if i == j:
            continue
        dist = (x1 - x2) ** 2 + (y1 - y2) ** 2
        if dist > max_:
            max_ = dist
            ans = j
    print(ans)
