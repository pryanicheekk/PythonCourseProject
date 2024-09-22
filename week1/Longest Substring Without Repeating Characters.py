class Solution(object):
    def lengthOfLongestSubstring(self, s):
        unique_list = []
        length = len(s)
        right_count = 0
        left_count = 0
        maximum = 0
        while right_count != length:
            if s[right_count] not in unique_list:
                unique_list.append(s[right_count])
                maximum = max(maximum, len(unique_list))
                right_count += 1
            else:
                for i in range(left_count, right_count):
                    if s[left_count] == s[right_count]:
                        right_count += 1
                        left_count += 1
                        break
                    else:
                        unique_list.remove(s[left_count])
                        left_count += 1
        return maximum
solution = Solution()
print(solution.lengthOfLongestSubstring("abdbvef"))