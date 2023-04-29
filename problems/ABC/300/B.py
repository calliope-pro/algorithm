# ABC300-B
# 脳死で左上のインデックスの位置から全探索した
import sys

rsl = lambda: list(sys.stdin.readline().rstrip())
rm = lambda: map(int, sys.stdin.readline().split())

h, w = rm()
am = [rsl() for _ in range(h)]
bm = [rsl() for _ in range(h)]
for di in range(h):
    for dj in range(w):
        flag = True
        for i in range(h):
            for j in range(w):
                if am[(i+di)%h][(j+dj)%w] != bm[i][j]:
                    flag = False
                    break
            if flag == False:
                break
        if flag:
            print('Yes')
            exit()
print('No')
