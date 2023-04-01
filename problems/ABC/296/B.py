# ABC296-B
# for文とインデックスの管理をしよう。`.index`メソッドは含有されてないとエラーになるので注意
import sys

rr = lambda: sys.stdin.readline().rstrip()

t = 'abcdefgh'
for i in range(8):
    s = rr()
    if '*' in s:
        c = s.index('*')
        print(f'{t[c]}{8-i}')
