class Solution:
    def reverseWords(self, s: str) -> str:
        ans = []

        i = len(s) - 1

        while i >= 0:

            # Skip spaces
            while i >= 0 and s[i] == " ":
                i -= 1

            if i < 0:
                break

            # End of word
            j = i

            # Find beginning of word
            while i >= 0 and s[i] != " ":
                i -= 1

            # Append the entire word
            ans.append(s[i + 1:j + 1])

        return " ".join(ans)