#再帰関数によるコイン支払いの可否
#n1 = int(input())
#coins = list(map(int, input().split()))
#x1 = int(input())
#def can_pay(n, x):
#    global coins
#    if n == 0:
#        if x == 0:
#            return True
#        else:
#            return False
#    elif can_pay(n-1, x):
#        """再帰関数、n個目を選ばない"""
#        return True
#    elif can_pay(n-1, x-coins[n-1]):
#        """再帰関数、n個目を選ぶ"""
#        return True
#    else:
#        return False
#if can_pay(n1, x1):
#    print('支払える')
#else:
#    print('支払えない')

#再帰関数にメモ要素要素を入れ、dp化したもの
n1 = int(input())
coins1 = list(map(int, input().split()))
x1 = int(input())
li = [-1]*(x1+1)
dp1 = [li]*(n1+1)
def can_pay(x, n, dp):
    if n == 0:
        if x == 0:
            return 1
        else:
            return 0
    elif x < 0:
        return 0
    
    if dp[n][x] != -1:
        return dp[n][x]
    elif can_pay(x-coins1[n-1], n-1, dp):
        dp[n][x] = 1
        return dp[n][x]
    elif can_pay(x, n-1, dp):
        dp[n][x] = 1
        return dp[n][x]
    else:
        dp[n][x] = 0
        return dp[n][x]
res = can_pay(x1, n1, dp1)
if res == 1:
    print(f'You can pay ${x1}')
else:
    print(f'You can\'t pay ${x1}')