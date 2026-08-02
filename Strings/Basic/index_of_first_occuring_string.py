class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0

        # Build LPS array
        lps = [0] * len(needle)
        length = 0
        i = 1

        while i < len(needle):
            while length > 0 and needle[i] != needle[length]:
                length = lps[length - 1]

            if needle[i] == needle[length]:
                length += 1

            lps[i] = length
            i += 1

        # KMP Search
        i = 0
        j = 0

        while i < len(haystack):
            while j > 0 and haystack[i] != needle[j]:
                j = lps[j - 1]

            if haystack[i] == needle[j]:
                j += 1

            if j == len(needle):
                return i - j + 1

            i += 1

        return -1