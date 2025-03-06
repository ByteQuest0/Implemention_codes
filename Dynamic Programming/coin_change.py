def coin_change(coins, amount):
    # Initialize dp array with infinity for all values
    # dp[i] represents the minimum number of coins needed to make amount i
    dp = [float('inf')] * (amount + 1)

    # Use an array to keep track of which coin was used for each amount
    coin_used = [None] * (amount + 1)

    # Base case: 0 coins needed to make amount 0
    dp[0] = 0

    # For each coin, calculate the minimum coins needed for each amount
    for coin in coins:
        # We can only use a coin for amounts >= coin value
        for current_amount in range(coin, amount + 1):
            # Try using the current coin and see if it gives a better solution
            if dp[current_amount - coin] + 1 < dp[current_amount]:
                dp[current_amount] = dp[current_amount - coin] + 1
                coin_used[current_amount] = coin

    # If dp[amount] is still infinity, it means the amount cannot be made with the given coins
    if dp[amount] == float('inf'):
        return -1, []

    # Backtrack to find which coins were used
    used_coins = []
    remaining = amount
    while remaining > 0:
        coin = coin_used[remaining]
        used_coins.append(coin)
        remaining -= coin

    return dp[amount], used_coins


# Example usage
coins = [1, 4, 6]
amount = 9
min_coins, coins_used = coin_change(coins, amount)

if min_coins == -1:
    print(f"Cannot make amount {amount} with the given coins")
else:
    print(f"Minimum coins needed to make {amount}: {min_coins}")
    print(f"Coins used: {coins_used}")
    print(f"Verification: {' + '.join(map(str, coins_used))} = {sum(coins_used)}")
