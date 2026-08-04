class Solution:
    def bagOfTokensScore(self, tokens: list[int], power: int) -> int:
        

        #sorting -> keep min power for buying score, max power for selling score
        tokens.sort()


        n = len(tokens)
        left = 0
        right = n - 1
        max_score = 0
        score = 0

        while (left <= right):

            if power >= tokens[left]:
                #buying the cheapest power score
                power -= tokens[left]
                score += 1
                max_score = max(max_score, score)
                left += 1
            elif score >= 1:
                #sell the most expensive score
                power += tokens[right]
                score -= 1
                right -= 1
            else:
                #we cannot buy nor sell
                break

        return max_score