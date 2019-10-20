def find_min_coins(available, S):
    available.sort()
    # use to store previous, smaller states
    sum_to_coins = {0: []}
    # best case for available coins is coin itself
    for c in available: sum_to_coins[c] = [c]
    for i in range(1, S+1):
        if i not in sum_to_coins:
            # base case is min_coin + previously seen
            for c in available:
                if c > i: break
                rem = i - c
                if rem not in sum_to_coins: continue
                if (i not in sum_to_coins or 
                        len(sum_to_coins[rem]) + 1 < len(sum_to_coins[i])):
                    sum_to_coins[i] = sum_to_coins[rem] + [c]
    print(sum_to_coins)
    return sum_to_coins[S]

res = find_min_coins([2, 3, 5], 11)
print(res)