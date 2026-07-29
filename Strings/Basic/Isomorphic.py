class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        #one to one mapping (bijection) that it
        #many to one and one to many mapping is mot allowed.

        #1st conditon , : - no. of unique characters must be equal, if not then not ismorphic
        #2nd condition: - one to one mapping only

        #maintaining to proper hashmaps() auto enforce the 1st condition

        #catches any mistmatch for one-> many mapping
        forward = {}

        #catches any mistmatch for many -> one mapping
        backward = {}

        if len(s) != len(t):
            return False
            
        for i in range(len(s)):

            c1 = s[i]
            c2 = t[i]

            #check if already mapped in forward  (s -> t)
            if c1 in forward:
                if forward[c1] != c2:
                    return False
            
            #if not , map it to c2
            else:
                forward[c1] = c2

            #reverse map: check if mapped in backward (t -> s)
            if c2 in backward:
                if backward[c2] != c1:
                    return False
            
            #if not , map it to c1
            else:
                backward[c2] = c1
        
        return True