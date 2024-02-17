def knapsack_01(P, W, C, n):
    dp = [[0 for _ in range(C + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):

        for w in range(C + 1):

            if W[i - 1] <= w:

                dp[i][w] = max(dp[i - 1][w], P[i - 1] + dp[i - 1][w - W[i - 1]])

            else:

                dp[i][w] = dp[i - 1][w]

    max_profit = dp[n][C]

    return max_profit


n = int(input("Enter the number of items: "))

P = [int(input(f"Enter profit for item {i + 1}: ")) for i in range(n)]

W = [int(input(f"Enter weight for item {i + 1}: ")) for i in range(n)]

C = int(input("Enter the capacity of the knapsack: "))

result = knapsack_01(P, W, C, n)

print(f"Maximum profit: {result}")