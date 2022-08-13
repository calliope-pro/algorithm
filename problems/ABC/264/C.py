# ABC264-C
# Python only
# bit全探索とnumpyで行列抽出が楽
import sys
import itertools
import numpy as np

rm = lambda: map(int, sys.stdin.readline().split())
rl = lambda: list(map(int, sys.stdin.readline().split()))

h_a, w_a = rm()
a = np.array([rl() for _ in range(h_a)])
h_b, w_b = rm()
b = np.array([rl() for _ in range(h_b)])

# npを使ったマスク・抽出
def f():
    for co_a in itertools.combinations(range(h_a), h_b):
        for co_b in itertools.combinations(range(w_a), w_b):
            if np.array_equal(a[np.ix_(co_a, co_b)], b):
                print('Yes')
                exit()
    print('No')

# スライスを使ったマスク・抽出
def f():
    for co_a in itertools.combinations(range(h_a), h_b):
        a_ = a[co_a, :]
        for co_b in itertools.combinations(range(w_a), w_b):
            if np.array_equal(a_[:, co_b], b):
                print('Yes')
                exit()
    print('No')

f()

