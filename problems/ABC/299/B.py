# ABC299-B
# すごい汚い
# 条件分岐を上手く実装するだけ
import sys

rm = lambda: map(int, sys.stdin.readline().split())
rl = lambda: list(map(int, sys.stdin.readline().split()))

n, t = rm()
t_ans = (0, 0)
o_ans = (0, 0)
cl_ = rl()
rl_ = rl()
oc = cl_[0]
for n, (c_, r_) in enumerate(zip(cl_, rl_), 1):
    if c_ == t:
        if t_ans[1] < r_:
            t_ans = (n, r_)
    elif oc == c_:
        if o_ans[1] < r_:
            o_ans = (n, r_)
if t_ans[0] != 0:
    print(t_ans[0])
else:
    print(o_ans[0])
