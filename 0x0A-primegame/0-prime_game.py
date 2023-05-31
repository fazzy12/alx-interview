#!/usr/bin/python3
"""Prime game module.
"""


def isWinner(x, nums):
    # Define a helper function to check if a number is prime


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


# Count the number of wins for each player
maria_wins = 0
ben_wins = 0

# Iterate over each round
for n in nums:
    primes = []
    # Generate a list of prime numbers up to n
    for i in range(2, n + 1):
        if is_prime(i):
            primes.append(i)

    # Determine the winner for the current round
    maria_turn = True
    while primes:
        selected_prime = primes.pop(0)
        primes = [p for p in primes if p % selected_prime != 0]
        maria_turn = not maria_turn

    if maria_turn:
        ben_wins += 1
    else:
        maria_wins += 1

# Determine the overall winner
if maria_wins > ben_wins:
    return "Maria"
elif ben_wins > maria_wins:
    return "Ben"
else:
    return None
