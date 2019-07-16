class Solution:
    def partitionLabels(self, S: str):
        self.groups = []
        self.char_locations = dict()
        self.sorted_bounds = []
        
        # O(N) find min and max indexes
        for i in range(len(S)):
            c = S[i]
            if c not in self.char_locations: 
                self.char_locations[c] = len(self.sorted_bounds)
                self.sorted_bounds.append([i, i])
            else: 
                index = self.char_locations[c]
                self.sorted_bounds[index][1] = i  # we know this is a new max
                
        # needs to be sorted by left bound
        for bound in self.sorted_bounds:
            self.insert_new(bound)
            
        return [(r - l + 1) for [l, r] in self.groups]
    
    def insert_new(self, bound):
        if self.groups == []: self.groups.append(bound)
        else:
            l, r = bound
            prev_l, prev_r = self.groups[-1]
            if l < prev_r:  # overlap
                self.groups.pop()
                self.insert_new([prev_l, max(r, prev_r)])
            
            else: self.groups.append(bound)


A = Solution()
# print(A.partitionLabels("aba"))
print(A.partitionLabels("ababcbacadefegdehijhklij"))