li = [] #[6, 8, 2, 7]
s = input('4桁の数を入力して下さい')
while len(s) != 4:
    s = input('4桁の数を入力して下さい')
li2 = []
t1 = int(input('0~30の整数を入力して下さい'))
lid = [0]*(t1+60)
dp1 = [lid]*5
for i in range(4):
    li.append(int(s[i]))
n1 = 4
def func(n, t, dp):
    if n == 1:
        if t == li[0]:
            return 1
        else:
            return 0

    if func(n-1, t+li[n-1], dp):
        li2.append('-')
        dp[n][t] = 1
        return dp[n][t]
    elif func(n-1, t-li[n-1], dp):
        li2.append('+')
        dp[n][t] = 1
        return dp[n][t]
    else:
        dp[n][t] = 0
        return dp[n][t]
if func(n1, t1, dp1):
    print("{0}{4}{1}{5}{2}{6}{3}={7}".format(li[0], li[1], li[2], li[3], li2[0], li2[1], li2[2], t1))
else:
    print("Sorry, we can't provide")