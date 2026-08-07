class LC5:
    def longestPalindrome(self, s: str) -> str:
        
        #lets cook with dp: since we have a len(s) of string as n , we need a dp matrix n*n
        #dp matrix : stores the indicies values indicating which is a plaindromic substring

        n = len(s)

        dp = [[False]*n for _ in range(n)]
        #intital values are kept at false:

        start = 0
        max_length = 1

        #base case : all single len substrings are plaindromes:
        for i in range(n):
            dp[i][i] = True

        
        #base case: checking for strings of len 2
        for i in range(n-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                start = i
                max_length = 2
        
        #solving for recurrence:
        #since length 1 and length 2 are alr filled , we start with 3, looping over lenghts:
        for length in range(3 , n+1):

            #generating all possible  substrings of this length
            for i in range(n-length +1):

                #position of j , ex : if  i = 0 , j = 2, ending index
                j = i + length - 1

                #check for recurrence : (palindrome condition)
                if s[i] == s[j] and dp[i+1][j-1]:
                    dp[i][j] = True

                    #check for max_len
                    if length > max_length:
                        start = i
                        max_length = length
            
        return s[start:start+max_length]



    def longestPalindrome2(self, s: str) -> str:
        
        if len(s) == 0:
            return ""

        #brute-force : generate every posible string and check for palindrome:

        max_len = 1   #smallest len for a palindrome is 1
        longest_palindrome = s[0]

        for i in range(len(s)):
            for j in range(i,len(s)):
                subString = s[i:j+1]

                if self.isPalindrome2(subString):
                    if len(subString) > max_len:
                        max_len = max(len(subString), max_len)
                        longest_palindrome = subString

        return longest_palindrome   
    
    def isPalindrome2(self, subString : str):
        left = 0
        right = len(subString) - 1

        while (left <= right):
            if subString[left] == subString[right]:
                left += 1
                right -= 1
            else:
                return False
        
        return True

    def longestPalindrome3(self, s: str) -> str:

        if not s:
            return ""

        memo = {}

        n = len(s)

        start = 0
        max_len = 1

        for i in range(n):
            for j in range(i, n):

                if self.ispalindrome3(s, i, j, memo):

                    curr_len = j - i + 1

                    if curr_len > max_len:
                        start = i
                        max_len = curr_len

        return s[start:start + max_len]

    def ispalindrome3(self, s, i, j, memo):

        #base case, we do not need to cache this , empty strings are also  planindrome
        if i >= j:
            return True

        #return if cached
        if (i, j) in memo:
            return memo[(i, j)]

        #if not cache , check for their validity of palindrome
        if s[i] != s[j]:
            memo[(i, j)] = False
        else:
            memo[(i, j)] = self.ispalindrome3(s, i + 1, j - 1, memo)

        return memo[(i, j)]

    def longestPalindrome4(self, s: str) -> str:

        if not s :
            return ""
        
        n = len(s)
        start = 0
        max_len = 1

        for i in range(n):
            #checking for odd center:
            l1, r1 = self.expand(s, i , i)
            curr_len  = r1-l1+1
            if curr_len > max_len:
                start = l1
                max_len = curr_len
            
            #checking for even center:

            l2 , r2 = self.expand(s, i , i +1)
            curr_len = r2- l2 +1
            if curr_len > max_len:
                start = l2
                max_len = curr_len
        
        return s[start:start + max_len]


    def expand(self, s: str , left : int , right : int):
        
        while  left >= 0  and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1

        #expanding out of bounds , so we return 1 index trimmed:
        return left +1 , right -1