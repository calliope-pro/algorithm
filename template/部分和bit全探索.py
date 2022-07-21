'''
5 13
1 2 3 5 6
'''
n, w = list(map(int, input().split()))
a_list = list(map(int, input().split()))
is_w = False
for bit in range(1, 1<<n):
    #bit = [1, 2^n)のフラグ
    li = []
    #bitのフラグの位置収納
    for i in range(0, n):
        #i = [0, n-1)のマスクビットの移動数
        if bit & 1<<i:
            #マスクビット
            li.append(i)
    s = 0
    for i in li:
        s += a_list[i]
    if s == w:
        is_w = True
        break
if is_w:
    print('Yes')
else:
    print('No')
    
