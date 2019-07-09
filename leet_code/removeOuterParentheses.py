# Time Limit Exceeded
class Solution1:
    def removeOuterParentheses(self, S: str) -> str:
        subgroups = []
        left = 0 
        for i in range(len(S)):
            c = S[i]
            if c == '(':
                left += 1  
                if left == 1:  # just beginning
                    subgroups.append([c, [left]])
                else:
                    # part of same subgroup
                    subgroups[-1][0] += c
                    subgroups[-1][1][-1] = left

            else:
                left -= 1
                subgroups[-1][0] += c
                if left == 1 and i < len(S) and S[i+1] == '(':
                    subgroups[-1][1].append(left)
        min_size = None
        for [s, sizes] in subgroups:
            sub_min = min(sizes)
            if min_size is None or sub_min < min_size:
                min_size = sub_min

        if min_size > 1: min_size -= 1  # deal with extra
        result = ''
        for [s, sizes] in subgroups:

            substr = s[min_size:len(s)-min_size]
            result += substr
        return result

class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        min_shells = None
        substr = ''
        while (min_shells is None or min_shells > 2):
            substr = ''
            left = 0
            sub_min = 1
            for c in S:
                if c == '(':
                    left += 1
                    if left > 1:  # outer shell
                        sub_min = max(sub_min, left)  # min is 2
                        substr += '('
                elif c == ')':
                    if left <= 0:
                        print('Wrongly matching parentheses')
                        return ''
                    elif left > 1:
                        substr += ')'
                        left -= 1
                    else:  # 1, closing the shell
                        left -= 1
                        if min_shells is None or min_shells > sub_min:
                            min_shells = sub_min

            if min_shells is None or min_shells > sub_min:
                min_shells = sub_min
        return substr

# New Attempt: Instead of while loop with O(N) so overall O(N^N), we can just create nested 
# lists of numbers, each sublist representing one subgroup
# (()())(())(()(())) -> [[1, 1], [1], [2]]



A = Solution1()

print(A.removeOuterParentheses('(()())(())'))
print(A.removeOuterParentheses('(()())(())(()(()))'))
print(A.removeOuterParentheses('()()'))

print(A.removeOuterParentheses("(((((())))))"))
                