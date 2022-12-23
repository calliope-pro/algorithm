# ABC282-A
# string.ascii_uppercase使うと楽
import sys
from string import ascii_uppercase as au

ri = lambda: int(sys.stdin.readline())

print(au[:ri()])
