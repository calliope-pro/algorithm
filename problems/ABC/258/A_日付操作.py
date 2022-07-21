import sys
from datetime import datetime, timedelta

ri = lambda: int(sys.stdin.readline())

n = datetime.today().replace(hour=21, minute=0)
print((n + timedelta(minutes=ri())).strftime('%H:%M'))
