def coin_change(coins, amount):
    dp = [0] + [float('inf')] * amount

    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[amount]


# Input
coins = [1, 2, 5]
amount = 11

# Find minimum number of coins
result = coin_change(coins, amount)

print("Coins:", coins)
print("Amount:", amount)
print("Minimum number of coins:", result)