import sys
import math
import itertools
import collections
import heapq
import re
import numpy as np

rr = lambda: sys.stdin.readline().rstrip()
rs = lambda: map(str, sys.stdin.buffer.readline().split())
ri = lambda: int(sys.stdin.buffer.readline())
rm = lambda: map(int, sys.stdin.buffer.readline().split())
rl = lambda: list(map(int, sys.stdin.buffer.readline().split()))

left = 1
right = 100 #[1, 100) 100は含まないことに注意
print('yes/noで答えてください')
while right - left > 1:
    mid = (right + left)//2
    print(f'あなたの年齢は{mid}才以上ですか')
    a = rr()
    if a == 'yes':
        left = mid
    elif a == 'no':
        right = mid
    else:
        print('yes/noで答えてください')
print(f'あなたは{left}才です')

