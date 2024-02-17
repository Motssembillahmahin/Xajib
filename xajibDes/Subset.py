def isSubsetSum(S, n, d):
    dp = [[False for _ in range(d + 1)] for _ in range(n + 1)]

    for i in range(n + 1):
        dp[i][0] = True

    for i in range(1, n + 1):

        for j in range(1, d + 1):

            if S[i - 1] > j:

                dp[i][j] = dp[i - 1][j]

            else:

                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - S[i - 1]]

    return dp[n][d]


S = list(map(int, input("Enter the array S (space-separated): ").split()))

d = int(input("Enter the target sum d: "))

n = len(S)

result = isSubsetSum(S, n, d)

if result:

    print("Subset with the sum", d, "exists.")

else:

    print("No subset with the sum", d, "exists.")