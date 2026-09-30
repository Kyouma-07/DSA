class LC1239:
    def maxLength(self, arr: list[str]) -> int:

        def backtrack(index, mask, length):
            ans = length

            for i in range(index, len(arr)):
                new_mask = mask
                valid = True

                for c in arr[i]:
                    bit = 1 << (ord(c) - ord('a'))

                    if new_mask & bit:
                        valid = False
                        break

                    new_mask |= bit

                if valid:
                    ans = max(ans,backtrack(i + 1,new_mask,length + len(arr[i])))

            return ans

        return backtrack(0, 0, 0)