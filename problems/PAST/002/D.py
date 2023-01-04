# PAST002-D
# ただただ集合にあり得るパターンを突っ込んだ
import sys

rr = lambda: sys.stdin.readline().rstrip()

s = rr()
set_ = set(['.'*i for i in range(1, min(4, len(s)+1))]) | set(list(s))
for i in range(len(s) - 1):
    tmp = s[i:i+2]
    set_.add(tmp)
    set_.add('.' + tmp[1])
    set_.add(tmp[0] + '.')

for i in range(len(s) - 2):
    tmp = s[i:i+3]
    set_.add(tmp)
    set_.add('..' + tmp[2])
    set_.add('.' + tmp[1] + '.')
    set_.add(tmp[0] + '..')
    set_.add('.' + tmp[1:])
    set_.add(tmp[0] + '.' + tmp[2])
    set_.add(tmp[:2] + '.')
print(len(set_))
