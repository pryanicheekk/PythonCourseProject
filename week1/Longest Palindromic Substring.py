class Solution(object):
    def longestPalindrome(self, s):
        if len(s) == 1:
            return s
        if len(s) == 2 and s[0] == s[1]:
            return s
        longest = s[0]
        for i in range(1, len(s) - 1):
            left = i - 1
            right = i + 1
            while (left >= 0 and right <= len(s) - 1):
                if s[left] == s[right]:
                    if (len(longest) < len(s[left:right + 1])):
                        longest = s[left:right + 1]
                    left -= 1
                    right += 1
                else:
                    break
        for i in range(len(s) - 1):
            left = i - 1
            right = i + 2
            if (s[i] == s[i + 1]):
                if (len(s[i:i + 2]) > len(longest)):
                    longest = s[i:i + 2]
                while (left >= 0 and right <= len(s) - 1):
                    if s[left] == s[right]:
                        if (len(s[left:right + 1]) > len(longest)):
                            longest = s[left:right + 1]
                        left -= 1
                        right += 1
                    else:
                        break
        return longest
solution = Solution()
print(solution.longestPalindrome("cbbd"))