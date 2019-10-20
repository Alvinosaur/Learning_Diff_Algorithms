# FUNCTIONAL DYNAMIC PROGRAMMING METHOD
def longestValidParentheses(s):
    substring_len = [0] * len(s)
    max_len =  0
    # skip i = 0 b/c impossible  to be 
    for i in range(1, len(s)):
        if s[i] == ')' and  s[i-1] == '(':
            if i == 1: substring_len[i] = 2
            # dynamic programming here: take previous adjacent substring's 
            # length (can be 0 if not a valid string) and add to cur result
            else: substring_len[i] = substring_len[i-2] + 2
        
        elif s[i] == ')' and s[i-1] == ')':
            # dynamic programming: if (()) nested structure, take 
            # length of inner to find the previous char
            inner_len = substring_len[i-1]
            # if char before inner substring is '(' then proper nest
            if s[i-inner_len-1] == '(':
                # this is the substring before the above '(' that we found
                # add inner length, also add 2 b/c of exterior nest
                substring_len[i] = (
                    substring_len[i-inner_len-2] + inner_len + 2)
        
        max_len = max(substring_len[i], max_len)
    return max_len


#  NON FUNCTIONAL ATTEMPT #1:
def longestValidParentheses2(s):
    valid_ranges = []
    cur_index = 0
    while(cur_index < len(s)):
        start, end = find_next_valid_substring(s, cur_index)
        if start != end: valid_ranges.append([start, end])
        cur_index = end + 1
    
    if len(valid_ranges) == 0: return ""
    longest_start, longest_end = valid_ranges[0][0], valid_ranges[0][1]
    i = 0
    print(valid_ranges)
    while(i < len(valid_ranges)-1):
        s1, e1 = valid_ranges[i]
        s2, e2 = valid_ranges[i+1]
        # if these two substrings adjacent, combine
        if e1 == s2 - 1:
            length = e2 - s1
            if length > (longest_end - longest_start):
                longest_start = s1
                longest_end = e2
            valid_ranges.remove([s2, e2])
            valid_ranges[i][1] = e2
        else:
            i += 1
        

    return s[longest_start:longest_end+1]


def find_next_valid_substring(s, start):
    num_left = 0
    count = 0
    for i in range(start, len(s)):
        if s[i] == '(':
            num_left += 1
        else:
            num_left -= 1
            count += 1
        if num_left ==  0:
            return (start, i)  # found end of next valid substring
        elif num_left < 0:
            return (start, start)
    
    # if reach this statement, we have a situation like (()
    print(count)
    return (len(s)-(count * 2), len(s)-1)
    


s = '(()()'
s1 = '()()'
s2 = '))()(())'
s3 = '"(()))())("'
print(longestValidParentheses(s3))