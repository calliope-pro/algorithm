# 典型90-072
# 普通に全探索+DFSでいい
# 一度通ったところは道としては通れない -> 最低でも4以上が答えなので、最後は条件分岐した
# 眠すぎて実装ぐだぐだ
import sys

rr = lambda: sys.stdin.readline().rstrip()
rm = lambda: map(int, sys.stdin.readline().split())

h, w = rm()
cm = [rr() for _ in range(h)]
passed = set()
def dfs(start_h, start_w, end_h, end_w, cnt=0):
    ans = -1
    for (dh, dw) in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        if 0 <= start_h+dh < h and 0 <= start_w+dw < w and cm[start_h+dh][start_w+dw] == '.' and (start_h+dh, start_w+dw) not in passed:
            if start_h+dh == end_h and start_w+dw == end_w:
                ans = max(cnt + 1, ans)
            passed.add((start_h+dh, start_w+dw))
            ans = max(dfs(start_h+dh, start_w+dw, end_h, end_w, cnt+1), ans)
            passed.discard((start_h+dh, start_w+dw))
    return ans

ans = -1
for i in range(h):
    for j in range(w):
        if cm[i][j] == '#':
            continue
        ans = max(dfs(i, j, i, j), ans)
print(ans if ans >= 4 else -1)



