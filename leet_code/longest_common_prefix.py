class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0: return ''
        for i in range(len(strs[0])):
            target_char = strs[0][i]
            for st in strs[1:]:
                if (i >= len(st) or 
                    st[i] != target_char):
                    return st[:i]
        return strs[0]
        
        

A = Solution()
print(A.longestCommonPrefix(['f', 'g']))
A.longestCommonPrefix([])