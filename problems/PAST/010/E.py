# PAST010-E
# 制約を見れば、高々1000年分 -> 全探索すればいい
import sys
from datetime import datetime, timedelta

year, month, day = map(int, sys.stdin.readline().split('/'))
date = datetime(year, month, day).date()
for _ in range(10**7):
    if len(set(date.strftime('%Y%m%d'))) <= 2:
        print(date.strftime('%Y/%m/%d'))
        exit()
    date += timedelta(days=1)
