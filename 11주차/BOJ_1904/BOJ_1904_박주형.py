# n = 1 > dp = 1 (1)
# n = 2 > dp = 2 (00, 11)
# n = 3 > dp = 3 (100, 001, 111)
# n = 4 > dp = 5 (0011, 0000, 1001, 1100, 1111)
# n = 5 > dp = 8 (00001,10000,11111,11001,10011,00111,11100,00100)

n = int(input())

dp = [0] * int(n+1)

for i in range(1, n+1):
    if i == 1:
        dp[i] = 1 % 15746
    elif i == 2:
        dp[i] = 2 % 15746
    else:
        dp[i] = (dp[i-1] + dp[i-2]) % 15746

print(dp[i])