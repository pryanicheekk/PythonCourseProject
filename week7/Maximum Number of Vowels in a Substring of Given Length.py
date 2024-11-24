class Solution(object):
    def maxVowels(self, s, k):
        ans = 0
        max_ans = 0
        for i in range(k):
            if s[i] in ['a','e','i','o','u']:
                ans+=1
                max_ans = max(max_ans,ans)
        if max_ans==k:
            return max_ans
        for i in range(k,len(s)):
            if s[i-k] in ['a','e','i','o','u']:
                flag  = 1
            else:
                flag = 0
            ans-= flag
            if s[i] in ['a','e','i','o','u']:
                ans+=1
                max_ans = max(max_ans,ans)
                if max_ans==k:
                    return k
        return max_ans
solution = Solution()
print(solution.maxVowels("leetcode",3))