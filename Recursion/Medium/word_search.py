from collections import Counter

class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:

        m, n = len(board), len(board[0])
        
        # 1. Capacity Pruning
        if len(word) > m * n:
            return False
            
        # 2. Frequency Pruning
        board_counts = Counter(char for row in board for char in row)
        for char, count in Counter(word).items():
            if board_counts[char] < count:
                return False
                
        # 3. Bigram Adjacency Pruning (The Large Board Optimization)
        # Collect all valid 2-character transitions that exist on the board
        valid_transitions = set()
        for r in range(m):
            for c in range(n):
                char = board[r][c]
                if r + 1 < m:
                    valid_transitions.add((char, board[r+1][c]))
                    valid_transitions.add((board[r+1][c], char))
                if c + 1 < n:
                    valid_transitions.add((char, board[r][c+1]))
                    valid_transitions.add((board[r][c+1], char))
                    
        # Check if the word requires a transition that isn't on the board
        for i in range(len(word) - 1):
            if (word[i], word[i+1]) not in valid_transitions:
                return False

        # 4. Reverse Optimization
        if board_counts[word[0]] > board_counts[word[-1]]:
            word = word[::-1]
            
        # 5. Standard DFS (In-place marking)
        def dfs(r, c, i):
            if i == len(word): return True
            if r < 0 or c < 0 or r >= m or c >= n or board[r][c] != word[i]: return False
                
            temp = board[r][c]
            board[r][c] = '#'
            
            res = (dfs(r+1, c, i+1) or dfs(r-1, c, i+1) or 
                dfs(r, c+1, i+1) or dfs(r, c-1, i+1))
                
            board[r][c] = temp
            return res
            
        for r in range(m):
            for c in range(n):
                if board[r][c] == word[0] and dfs(r, c, 0):
                    return True
                    
        return False