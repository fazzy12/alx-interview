def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def isWinner(x, nums):
    wins = [0, 0]  # Maria's wins and Ben's wins

    for num in nums:
        turn = 0  # 0 for Maria, 1 for Ben
        primes = [p for p in range(2, num + 1) if is_prime(p)]

        while primes:
            if turn == 0:  # Maria's turn
                for prime in primes:
                    if prime <= num:
                        primes = [p for p in primes if p % prime != 0]
                        wins[0] += 1
                        turn = 1  # Switch to Ben's turn
                        break
            else:  # Ben's turn
                for prime in primes:
                    if prime <= num:
                        primes = [p for p in primes if p % prime != 0]
                        wins[1] += 1
                        turn = 0  # Switch to Maria's turn
                        break

    if wins[0] > wins[1]:
        return "Maria"
    elif wins[0] < wins[1]:
        return "Ben"
    else:
        return None
