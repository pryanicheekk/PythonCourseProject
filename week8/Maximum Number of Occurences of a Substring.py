import collections
class Solution(object):
    def maxFreq(self, s, maxLetters, minSize, maxSize):
        count = collections.Counter()

        for i in range(len(s) - minSize + 1):
            t = s[i: i + minSize]
            if len(set(t)) <= maxLetters:
                count[t] += 1

        if count:
            return max(count.values())
        else:
            return 0
solution = Solution()
print(solution.maxFreq("aababcaab", 2, 3, 4))