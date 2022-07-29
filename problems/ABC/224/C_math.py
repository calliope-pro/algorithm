# PyPy only
import sys
import itertools

ri = lambda: int(sys.stdin.readline())
rm = lambda: map(int, sys.stdin.readline().split())
def calc_triangle_area(x0, y0, x1, y1, x2, y2):
    area = (x1 - x0)*(y2 - y0) - (x2 - x0)*(y1 - y0)
    area = 1/2 * abs(area)
    return area

n = ri()
xy = []
for _ in range(n):
    x, y = rm()
    xy.append((x, y))

cnt = 0
for co in itertools.combinations(xy, 3):
    area = calc_triangle_area(co[0][0], co[0][1], co[1][0], co[1][1], co[2][0], co[2][1])
    if area != 0:
        cnt += 1
print(cnt)
