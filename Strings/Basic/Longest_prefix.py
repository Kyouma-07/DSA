class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        
        #checking colmns
        for i in range(len(strs[0])):

            ch = strs[0][i]

            for word in strs[1:]:
                if i == len(word) or word[i] != ch:
                    return strs[0][:i]
            
        return strs[0]

    def longestCommonPrefix2(self, strs: list[str]) -> str:
        
        #using startswith() function

        prefix = strs[0]

        for word in strs[1:]:
            while not word.startswith(prefix):
                prefix = prefix[:-1]

                if not prefix:
                    return ""
        
        return prefix