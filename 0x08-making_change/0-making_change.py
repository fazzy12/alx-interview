#!/usr/bin/python3

def makeChange(coins, total):
if total < 0:
    return -1

# Create a list to store the minimum number of coins needed for each amount
# Initialize the list with a value larger than the total amount
dp = [float('inf')] * (total + 1)
    
# Base case: 0 coins needed for a total of 0
dp[0] = 0

# Iterate through each coin value
for coin in coins:
    # For each amount from the coin value to the total
    for amount in range(coin, total + 1):
        # Update the minimum number of coins needed if the current coin is used
        dp[amount] = min(dp[amount], dp[amount - coin] + 1)

# If the minimum number of coins for the total is still larger than the total,
# it means the total cannot be met by the given coins
return dp[total] if dp[total] != float('inf') else -1
