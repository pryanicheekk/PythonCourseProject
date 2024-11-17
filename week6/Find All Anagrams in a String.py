class Solution(object):
    def findAnagrams(self, s, p):
        def func(string):
            a = [0] * 26
            for i in range(len(string)):
                a[ord(string[i]) - ord('a')] += 1
            return a

        answer = []
        p_list = func(p)
        s_list = func(s[0:len(p)])
        if p_list == s_list:
            answer.append(0)
        for i in range(1, len(s) - len(p) + 1):
            s_list[ord(s[i - 1]) - ord('a')] -= 1
            s_list[ord(s[i + len(p) - 1]) - ord('a')] += 1
            if s_list == p_list:
                answer.append(i)
        return answer
solution = Solution()
print(solution.findAnagrams("cbaebabacd","abc"))