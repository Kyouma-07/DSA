class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        
        #potate- solution:

        freq = {}

        for ch in word:
            freq[ch] = freq.get(ch,0) +1
        
        print(freq)

        for row in board:
            print(row)
            for ch in word:
                if ch in row:
                    if freq[ch] != 0:
                        freq[ch] -= 1
                else:
                    continue
        print(freq)
        
        for value in freq.values():
            if value > 0:
                return False
        else:
            return True


obj = Solution()
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
print(obj.exist(board, "ABCB"))