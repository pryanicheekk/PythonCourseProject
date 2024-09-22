class Solution(object):
    def reverseWords(self, s):
        answer_list = []
        answer = ""
        length = len(s)
        count=0
        while count<length:
            if s[count]==" ":
                count+=1
            else:
                curr = ""
                while (s[count] not in " "):
                    curr+=s[count]
                    count+=1
                    if count==length:
                        break
                answer_list.append(curr)
        for i in range (len(answer_list)-1,-1,-1):
            answer+=answer_list[i]
            answer+=" "
        return answer
solution = Solution()
print(solution.reverseWords("the sky is blue"))