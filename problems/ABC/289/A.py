# ABC289-A
# .replaceは同期処理なので、中間変数を入れる必要がある
# 別の方法で1度で変換も可能だが、コーディングに時間がかかる
import sys

rr = lambda: sys.stdin.readline().rstrip()

print(rr().replace(*'02').replace(*'10').replace(*'21'))
