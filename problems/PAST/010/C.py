# PAST010-C
# 規則を見極めて数学的にする
import sys
import math
from string import ascii_lowercase, ascii_uppercase

rr = lambda: sys.stdin.readline().rstrip()
al = ascii_lowercase

alpha = rr()
c = al[math.ceil(len(alpha)/3) - 2]
print(alpha[:len(alpha) - 3*(math.ceil(len(alpha)/3) - 1)] + c)
