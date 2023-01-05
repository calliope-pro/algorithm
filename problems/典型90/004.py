# 典型90-004
# 縦と横の和をそれぞれ事前に計算し、最後にシミュレーションする
import sys

rm = lambda: map(int, sys.stdin.readline().split())
rl = lambda: list(map(int, sys.stdin.readline().split()))

h, w = rm()
hl = [0] * h
wl = [0] * w
a_mat = []

for idx_h in range(h):
    al = rl()
    hl[idx_h] = sum(al)
    for idx_w, av in enumerate(al):
        wl[idx_w] += av
    a_mat.append(al)

for idx_h in range(h):
    ans = []
    for idx_w in range(w):
        ans.append(hl[idx_h] + wl[idx_w] - a_mat[idx_h][idx_w])
    print(*ans)
