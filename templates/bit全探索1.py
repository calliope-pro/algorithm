n, m, k = map(int, input().split())
li = []
for t in range(n):
    li.append(list(map(int, input().split())))
price_list = []
for bit in range(1, 2**n):
    index_list = []
    for i in range(n):
        if bit & 1<<i:
            index_list.append(i)

    c = 0
    for t in range(1,m+1):
        s = 0
        for i in index_list:
            s += li[i][t]
        if s >= k:
            c += 1
        else:
            break

    if c == m:
        p = 0
        for i in index_list:
            p += li[i][0]
        price_list.append(p)

if len(price_list):
    print(min(price_list))
else:
    print('-1')
        
