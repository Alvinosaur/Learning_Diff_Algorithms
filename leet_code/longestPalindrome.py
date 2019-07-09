import time

# too slow, fails on aaaaaaa.... x 1000
def longestPalindrome(s: str) -> str:
    if len(s) == 0: return s
    pair_mapping = dict()
    # O(N)
    for i in range(len(s)):
        char = s[i]
        if char not in pair_mapping.keys():
            pair_mapping[char] = [i]
        else:
            pair_mapping[char].append(i)

    pairs = []
    for indexes in pair_mapping.values():
        for i in range(len(indexes)):
            for j in range(i+1, len(indexes)):
                found_pair = True
                pairs.append( (min(indexes[i], indexes[j]), max(indexes[i], indexes[j])) )
    pairs.sort(key = lambda x : abs(x[1] - x[0]))
    for i in range(len(pairs)):
        pair = pairs[len(pairs) - i - 1]
        (j, k) = pair
        success =  True
        while (k - j >= 1):
            if s[j] != s[k]:
                success = False
                break
            j += 1
            k -= 1
        if (success): return s[pair[0]:pair[1]+1]
    return s[0]

    # print(pair_mapping)

def isPalindrome(s, i, j, mapping):
    while (j - i >= 1):
        if (i, j) in mapping:
            return mapping[(i, j)]
        if s[i] != s[j]: return False
        i += 1
        j -= 1
    return True

def longestPalindrome2(s: str) -> str:
    if s == "": return ""
    pair_mapping = dict()
    result_i = 0
    result_j = 0
    max_len = 0
    for i in range(len(s)):
        for j in range(i+1, len(s)):
            if isPalindrome(s, i, j, pair_mapping):
                pair_mapping[(i, j)] = True
                if j - i > max_len:
                    result_i = i
                    result_j = j
                    max_len = j - i
            else: pair_mapping[(i, j)] = False
    return s[result_i:result_j+1]

s = 'ababababab'
for i in range(100):
    start = time.time()
    longestPalindrome2(s)
    end = time.time()
    print(end - start, len(s))
    s += 'ababababab'