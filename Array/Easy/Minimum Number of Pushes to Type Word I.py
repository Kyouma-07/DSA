class LC3014:

    def __init__(self):
        pass

    def minimumPushes(self, word: str) -> int:

        n = len(word)
        total_pushes = 0

        batches = n // 8

        for i in range(1, batches + 1):
            total_pushes += i * 8
        
        # Remaining characters:
        remainder = n % 8
        remainder_multiplier = batches + 1  # n // 8 + 1
        total_pushes += remainder * remainder_multiplier

        return total_pushes

    
    def minimumPushes2(self, word: str) -> int:
        total_pushes = 0
        for i in range(0 , len(word)):
            multiplier = i // 8 + 1
            total_pushes += multiplier
        
        return total_pushes