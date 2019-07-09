import time

# naive recursion b/c passes the same situation multiple times
def minChange(coins: set, change: int) -> int:
	# Base case: perfect amount of change matching one coin
	if change in coins: return 1 
	# Have to search all the coins and try each recursively
	possible_coins = set([c for c in coins if c < change])
	min_coins = -1
	for c in possible_coins:
		guess = 1 + minChange(possible_coins, change - c)
		if min_coins < 0 or guess < min_coins:
			min_coins = guess
	return min_coins

start = time.time()
# print(minChange({1, 5, 10, 25}, 63), 'elapsed time: ', time.time() - start)


# memoization/caching version
def minChange(coins: set, change: int, sol_map=dict()) -> int:
	# Base case: perfect amount of change matching one coin
	if change in coins: 
		sol_map[change] = 1
		return 1 
	elif sol_map.get(change) != None:
		return sol_map[change]
	# Have to search all the coins and try each recursively
	possible_coins = set([c for c in coins if c < change])
	min_coins = -1
	for c in possible_coins:
		guess = 1 + minChange(possible_coins, change - c, sol_map)
		if min_coins < 0 or guess < min_coins:
			min_coins = guess
			sol_map[change] = min_coins
	return min_coins

start = time.time()
print(minChange({1, 5, 10, 25}, 63), 'elapsed time: ', time.time() - start)


# dynamic programming version:
"""
In the above, we worked top-down from high amounts of change down to small amounts and updated our
dict along the way. It used recursion to reach down to small amounts to the end.

In dynamic programming, work from bottom-up by starting with small amount of change and working upwards,
and this guarantees that we do indeed see previous results with smaller amounts of change.

"""
def DminChange(coins: set, change: int, sol_map=dict()) -> int:
	# find solutions to all <= amounts of change and work upwards
	for subChange in range(change+1):
		# use <= here since we aren't checking if change in coins
		possible_coins = set([c for c in coins if c <= change])
		minChangeAmt = subChange  # max is all pennies for given amount of change
		sol_map[subChange] = subChange   # initially worse-case
		for c in possible_coins:
			if sol_map.get(subChange - c) != None:  #  seen this before
				# if prev seen sol +1 extra coin is a better solution
				if sol_map[subChange - c] + 1 < minChangeAmt:  
					minChangeAmt = sol_map[subChange - c] + 1
			else: 
				sol_map[subChange - c] = minChangeAmt
		sol_map[subChange] = minChangeAmt
	return sol_map[subChange]

print(DminChange({1, 5, 10, 25}, 63), 'elapsed time: ', time.time() - start)