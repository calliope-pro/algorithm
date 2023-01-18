# ABC243-D
# 愚直にループして計算するとTLE
# LRしたあとにUすると元に戻るという性質を使う。回り道しない演算になるため、計算量が減る
# 2倍の演算なので、2進数として文字列に0,1を加えたりする方法も良い
import queue
import sys

rr = lambda: sys.stdin.readline().rstrip()
rm = lambda: map(int, sys.stdin.readline().split())

n, x = rm()
s = rr()
stack_lr = queue.LifoQueue()
for c in s:
    if c == 'U':
        if stack_lr.qsize():
            c_ = stack_lr.get()
        else:
            x //= 2
    else:
        stack_lr.put(c)
for c in stack_lr.queue:
    x *= 2
    if c == 'R':
        x += 1
print(x)
