# ABC348-A
# ooxooxの並びからn文字取り出すと楽
import sys

ri = lambda: int(sys.stdin.readline())

n = ri()
print(('oox'*100)[:n])
