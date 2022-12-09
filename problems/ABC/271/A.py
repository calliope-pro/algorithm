# ABC271-A
# 余りと商を上手く組み合わせる
# string.hexdigitsを使いべた書きを減らす
import sys
from string import hexdigits

ri = lambda: int(sys.stdin.readline())

n = ri()
a = n // 16
b = n % 16
print(f'{hexdigits[a]}{hexdigits[b]}'.upper())
