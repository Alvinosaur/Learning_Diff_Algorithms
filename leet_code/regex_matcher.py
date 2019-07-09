class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if p == '': return (s == '')
        if s == '': return (p == '' or p == '.' or (len(p) > 1 and p[1] == '*'))
        foundMatch = (len(s) > 0 and (s[0] == p[0]) or p[0] == '.')
        if len(p) > 1 and p[1] == '*':
            # need to deal with two possible cases, one if there isn't this repeat character
            # or if there are many of this repeating character
            return ((s == '' and len(p) == 2) or 
                    (self.isMatch(s, p[2:])) or 
                    (foundMatch and self.isMatch(s[1:], p)))
        return foundMatch and self.isMatch(s[1:], p[1:])
    

a = Solution()
print(a.isMatch('ab', '.*c'))