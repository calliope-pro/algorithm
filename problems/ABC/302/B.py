# ABC302-B
# 問題読みにくすぎだろ
# クソ実装かましてけ 😃
# snukeになるかekunsになるかなので、全部調べ上げる
import sys

rr = lambda: sys.stdin.readline().rstrip()
rm = lambda: map(int, sys.stdin.readline().split())

h, w = rm()
sm = [rr() for _ in range(h)]
s = 'snuke'
t = 'ekuns'
for r in range(h):
    for c in range(w):
        if sm[r][c] != 's' and sm[r][c] != 'e':
            continue
        if c+5 <= w:
            s_ = sm[r][c:c+5]
            if s_ == s:
                for i in range(5):
                    print(r+1, c+1+i)
                exit()
            if s_ == t:
                for i in range(5):
                    print(r+1, c+5-i)
                exit()
        if r+5 <= h:
            s_ = ''.join(sm[r+i][c] for i in range(5))
            if s_ == s:
                for i in range(5):
                    print(r+1+i, c+1)
                exit()
            if s_ == t:
                for i in range(5):
                    print(r+5-i, c+1)
                exit()
        if c+5 <= w and r+5 <= h:
            s_ = ''.join(sm[r+i][c+i] for i in range(5))
            if s_ == s:
                for i in range(5):
                    print(r+1+i, c+1+i)
                exit()
            if s_ == t:
                for i in range(5):
                    print(r+5-i, c+5-i)
                exit()
        if 0 <= c-4 and r+5 <= h:
            s_ = ''.join(sm[r+i][c-i] for i in range(5))
            if s_ == s:
                for i in range(5):
                    print(r+1+i, c+1-i)
                exit()
            if s_ == t:
                for i in range(5):
                    print(r+5-i, c-3+i)
                exit()
