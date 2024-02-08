import sys

rm = lambda: map(int, sys.stdin.readline().split())

h, w, n = rm()
m = [[0]*w for _ in range(h)]
now = [0, 0, 0]  # 上:0, 右:1, 下:2, 左:3
for _ in range(n):
    h_, w_, dir = now
    now[-1] = (dir + (-1)**m[h_][w_]) % 4
    m[h_][w_] ^= 1
    if now[-1] == 0:
        now[0] -= 1
        now[0] %= h
    elif now[-1] == 1:
        now[1] += 1
        now[1] %= w
    elif now[-1] == 2:
        now[0] += 1
        now[0] %= h
    else:
        now[1] -= 1
        now[1] %= w
print(*(''.join(map(lambda a: ".#"[a], m_)) for m_ in m), sep="\n")
