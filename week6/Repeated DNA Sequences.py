class Solution(object):
    def findRepeatedDnaSequences(self, s):
        m = {}
        for i in range(len(s)):
            m[s[i : i + 10]] = 1 + m.get(s[i : i + 10], 0)
        return [key for key, value in m.items() if value > 1]
solution = Solution()
print(solution.findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))