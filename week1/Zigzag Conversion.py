class Solution(object):
    def convert(self, s, numRows):
        strings = [""] * numRows
        if (numRows == 1):
            return s
        length = len(s)
        if (numRows >= length):
            return s
        count = 0
        lenZig = numRows*2-2
        answer = ""
        while(count!=length):
            ost = count%lenZig
            if (ost<numRows):
                strings[ost]+=s[count]
                count+=1
            else:
                strings[lenZig-ost]+=s[count]
                count+=1
        for i in range (numRows):
            answer+=strings[i]
        return answer
solution = Solution()
print(solution.convert("geeksforgeeks",3))