# ABC308-D
# dfsでゴリ押し！
import sys
from functools import lru_cache

rsl = lambda: list(sys.stdin.readline().rstrip())
rm = lambda: map(int, sys.stdin.readline().split())

sys.setrecursionlimit(10000000)

h, w = rm()
sm = [rsl() for _ in range(h)]
next_dict = {
    's': 'n',
    'n': 'u',
    'u': 'k',
    'k': 'e',
    'e': 's'
}
passed = {(0, 0)}
@lru_cache(None)
def dfs(x=0, y=0):
    next_str = next_dict[sm[x][y]]
    if x == h-1 and y == w-1:
        return 1

    ans = 0
    for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1)):
        if 0 <= x+dx < h and 0 <= y+dy < w and (x+dx, y+dy) not in passed and sm[x+dx][y+dy] == next_str:
            passed.add((x+dx, y+dy))
            ans = max(dfs(x+dx, y+dy), ans)
    return ans
if sm[0][0] != 's':
    print('No')
    exit()
if dfs(0, 0) == 1:
    print('Yes')
else:
    print('No')
