# ABC295-B
# 制限が小さいので、2次行列を2重ループで全探索してもヨシ！
import sys
import itertools

rsl = lambda: list(sys.stdin.readline().rstrip())
rm = lambda: map(int, sys.stdin.readline().split())

r, c = rm()
bm = [rsl() for _ in range(r)]
for i, j in itertools.product(range(r), range(c)):
    bm_i_j = bm[i][j]
    if bm_i_j != '.' and bm_i_j != '#':
        bi = int(bm_i_j)
        for i_, j_ in itertools.product(range(r), range(c)):
            if (abs(i-i_) + abs(j-j_)) <= bi and bm[i_][j_] == '#':
                bm[i_][j_] = '.'
        bm[i][j] = '.'
for bl in bm:
    print(''.join(bl))
