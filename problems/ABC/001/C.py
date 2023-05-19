# ABC001-C
# クソ問。今からしたら誤差の処理適当すぎるやろ。。。
import sys

rm = lambda: map(int, sys.stdin.readline().split())
inf = float('inf')

deg, dis = rm()

dis_s = round((dis+0.01)/6)
li = [2, 15, 33, 54, 79, 107, 138, 171, 207, 244, 284, 326, inf]
for i, v in enumerate(li):
    if dis_s <= v:
        w = i
        break
if w == 0:
    print('C', 0)
    exit()
deg = (10*deg + 1125) // 2250
dir_list = ['N', 'NNE', 'NE', 'ENE', 'E', 'ESE', 'SE', 'SSE', 'S', 'SSW', 'SW', 'WSW', 'W', 'WNW', 'NW', 'NNW', 'N']
print(dir_list[deg], w)
