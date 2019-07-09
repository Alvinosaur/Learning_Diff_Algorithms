import copy

def print_perms(s):
	sol = []
	for i in range(len(s)):
		s0 = s[i]
		remainder = s[:i] + s[i+1:]
		sol += print_perms(remainder)
		for j in range(len(remainder)+1):
			sol.append(remainder[:j] + s0 + remainder[j:])

	return sol

def powerset(a):
    # base case
    if (len(a) == 0): return [[]]
    else:
        result = []
        singleton = a[0]
        for subset in powerset(a[1:]):
            # subset itself
            result.append(subset)
            
            # singleton + subset
            result.append([singleton] + subset)
        return result


def powerstring(s):
    if len(s) == 0: return ['']
    else:
        combos = set()
        for i in range(len(s)):
	        single = s[i]
	        combos.add(single)
	        for substr in powerstring(s[:i] + s[i+1:]):
	            combos.add(substr)
	            if len(substr) != 0: combos.add(single + substr)
        return combos

def powerstring_wrong(s):
    if len(s) == 0: return ['']
    else:
        combos = set()
        single = s[0]
        for substr in powerstring(s[1:]):
            combos.add(substr)
            combos.add(single + substr)
            combos.add(substr + single)
        return combos
        
# print(powerset([1,2,3]))

# print(powerset([1,2,3]))

print(len(powerstring('AAABBC')))