# ABC267-A
# 文字全ての比較がだるいので、3文字目で比較し、インデックスから求めた
import sys

rr = lambda: sys.stdin.readline().rstrip()

s = rr()[2]
li = ['n', 'e', 'd', 'u', 'i']
li.reverse()
print(li.index(s)+1)
