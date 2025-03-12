def countWays(coins, target):
    dp = [0] * (target + 1)  # DP table, where dp[i] stores ways to make amount i
    dp[0] = 1  # Base case: There's 1 way to make amount 0 (by choosing nothing)

    for coin in coins:  # Iterate over each coin
        for amount in range(coin, target + 1):  # Update dp array for each amount
            dp[amount] += dp[amount - coin]  # Include current coin

    return dp[target]  # Return ways to form `target`

# Example usage:
coins = [1, 2, 5]
target = 5
print(countWays(coins, target))  # Output: 4
