class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        count_freq = {}

        for i in magazine:
            if i in count_freq:
                count_freq[i] += 1
            else:
                count_freq[i] = 1
        
        for ch in ransomNote:
            if ch not in count_freq or count_freq[ch] == 0:
                return False
            count_freq[ch] -= 1
        
        return True