class LC344:

    #recursion
    def reverseString1(self, s: list[str]) -> None:
            def helper(left, right):
                if left >= right:
                    return

                s[left], s[right] = s[right], s[left]
                helper(left + 1, right - 1)

            helper(0, len(s) - 1)


    #2-pointers
    def reverseString2(self, s: list[str]) -> None:
     
     left = 0
     right = len(s) -1

     while (left < right):
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1


        