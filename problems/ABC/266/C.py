# ABC266-C
# 凸性をそれぞれ判定すればいい
# 4辺しか無いのでべた書きした
import sys

rm = lambda: map(int, sys.stdin.readline().split())

class GeometryHandler:
    @classmethod
    def calc_triangle_area(cls, x0, y0, x1, y1, x2, y2) -> int:
        '''
        3点より三角形の面積を算出

        Parameters
        ----------
        x0, y0 : int
            点(x0, y0)となる
        x1, y1 : int
            点(x1, y1)となる
        x2, y2 : int
            点(x2, y2)となる

        Returns
        -------
        int
            三角形の面積
        '''
        area = (x1 - x0)*(y2 - y0) - (x2 - x0)*(y1 - y0)
        area = 1/2 * abs(area)
        return area

    @classmethod
    def is_convex(cls, x0, y0, x1, y1) -> bool:
        '''
        隣接する2辺に関する凸性判定

        Parameters
        ----------
        x0, y0 : int
            0度の基準となる辺・ベクトル
            (x0, y0)となる辺・ベクトル
        x1, y1 : int
            (x1, y1)となる辺・ベクトル

        Returns
        -------
        bool
            凸性の有無
            (x0, y0)から反時計回りに180度以上ならば凸性が認められずFalse
        '''
        return (x0*y1 - x1*y0) > 0

ax, ay = rm()
bx, by = rm()
cx, cy = rm()
dx, dy = rm()

if (GeometryHandler.is_convex(cx-bx, cy-by, ax-bx, ay-by)
    and GeometryHandler.is_convex(dx-cx, dy-cy, bx-cx, by-cy)
    and GeometryHandler.is_convex(ax-dx, ay-dy, cx-dx, cy-dy)
    and GeometryHandler.is_convex(bx-ax, by-ay, dx-ax, dy-ay)):
    print('Yes')
else:
    print('No')
