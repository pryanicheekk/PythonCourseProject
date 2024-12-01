class Solution(object):
    def numberOfSubstrings(self, s):
        map = {}
        count = 0
        start = end = 0
        n = len(s)
        while end < n:
            map[s[end]] = map.get(s[end], 0) + 1
            while map.get('a', 0) > 0 and map.get('b', 0) > 0 and map.get('c', 0) > 0:
                count += n - end
                map[s[start]] -= 1
                start += 1
            end += 1
        return count
solution = Solution()
print(solution.numberOfSubstrings("abcabc"))