# PAST001-A
# 例外処理を用いた
import sys

ri = lambda: int(sys.stdin.readline())

try:
    print(ri()*2)
except:
    print('error')
