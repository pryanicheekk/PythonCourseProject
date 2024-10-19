class Solution(object):
    def groupAnagrams(self, strs):
        dic = {}
        k = []
        for i in strs:
            l = "".join(sorted(i))
            dic.setdefault(l, []).append(i)

        return dic.values()
solution = Solution()
print(solution.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))