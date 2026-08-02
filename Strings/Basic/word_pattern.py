class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        words = s.split()

        if len(words) != len(pattern):
            return False
        
        char_to_word = {}
        word_to_char = {}

        for i in range(len(pattern)):
            ch = pattern[i]
            word = words[i]

            #map
            if ch in char_to_word:
                if char_to_word[ch] != word:
                    return False
                
            else:
                char_to_word[ch] = word
            
            if word in word_to_char:
                if word_to_char[word] != ch:
                    return False
            
            else:
                word_to_char[word] = ch
        
        return True

            
