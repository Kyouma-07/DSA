class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        
        #if goal if a rotation of s  , it must appear as a substring s + s
        return len(s) == len(goal) and goal in (s + s)