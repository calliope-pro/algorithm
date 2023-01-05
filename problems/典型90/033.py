# 典型90-033
# 4*4や3*5のそれぞれでの下界と上界を考えると法則性に気付く
# 2x2のマスが対象 -> コーナーケースを考える
import sys
import math

rm = lambda: map(int, sys.stdin.readline().split())

h, w = rm()
if h == 1 or w == 1:
    print(h*w)
else:
    print(math.ceil(h/2) * math.ceil(w/2))
