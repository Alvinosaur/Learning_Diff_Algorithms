
"""Dynamic Programming:
- start off from smaller elements, work your way up to target
- try all possible values <= current i
	- for each, calculate the remainder, use a dictionary to lookup this remainder and the number of coins required for it, then see if this and current possible value <= min for this current number
"""
def fib_memoization(n):
	lookup = dict()
	
	def fib_helper(n):
		if n not in lookup:
			if n <= 1: lookup[n] = n
			else: lookup[n] = fib_helper(n-1) + fib_helper(n-2)
		return lookup[n]

	return fib_helper(n)

def fib_tabulated(n):
	"""Problem: have to compute every single element,  whereas with memoization,
	you wouldn't have to do this.
	
	Arguments:
		n {[type]} -- [description]
	
	Returns:
		[type] -- [description]
	"""
	results = [0, 1]
	for i in range(2, n+1):
		results.append(results[i-1] + results[i-2])

	return results[n]

print(fib_memoization(9))
print(fib_tabulated(9))


"""Binary Search: O(logN): require sorted array, start with middle, if target > middle, only look at right side of array, vice versa for left.
"""
