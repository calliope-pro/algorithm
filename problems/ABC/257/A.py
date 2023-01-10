# ABC257-A
# math.ceil関数を使うと何番目のグループか分かる
import sys
import math
from string import ascii_uppercase

rm = lambda: map(int, sys.stdin.readline().split())
au = ascii_uppercase

n, x = rm()
print(au[math.ceil(x/n) - 1])
