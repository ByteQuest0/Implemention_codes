def knapsack(weights, profits, capacity):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    # Build DP table
    for i in range(1, n + 1):  # Items
        for w in range(capacity + 1):  # Capacity from 0 to W
            if weights[i-1] > w:  # If item is too heavy, exclude it
                dp[i][w] = dp[i-1][w]
            else:
                dp[i][w] = max(dp[i-1][w], profits[i-1] + dp[i-1][w - weights[i-1]])

    # Find selected items
    w = capacity
    selected_items = []
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:  # If the value changed, the item was included
            selected_items.append(i-1)  # Store item index
            w -= weights[i-1]

    selected_items.reverse()  # To get items in order

    return dp[n][capacity], selected_items

# Example usage:
weights = [3, 2, 4, 5, 1]
profits = [50, 40, 70, 80, 10]  
capacity = 7

max_profit, items = knapsack(weights, profits, capacity)
print("Maximum Profit:", max_profit)
print("Items in Knapsack:", items)  
