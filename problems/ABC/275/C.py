# ABC275-C
# 高々81^4 -> 全探索でいい
# 集合とタプルを使って存在判定する
# 重複がある分をきちんと考慮する
import sys

rr = lambda: sys.stdin.readline().rstrip()

s = [rr() for _ in range(9)]
sets = set()
for y in range(9):
    for x in range(9):
        if s[y][x] == '#':
            sets.add((x, y))
cnt = 0
for (now_x, now_y) in sets:
    for (next_x, next_y) in sets:
        dx = next_x - now_x
        dy = next_y - now_y
        if dx == 0 and dy == 0:
            continue
        if (next_x-dy, next_y+dx) in sets and (now_x-dy, now_y+dx) in sets:
            cnt += 1
print(cnt // 4)
