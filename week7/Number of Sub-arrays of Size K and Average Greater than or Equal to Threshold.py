class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
        ans = 0
        average = 0
        for i in range(k):
            average+=arr[i]
        average/=k
        if average>=threshold:
            ans+=1
        for i in range(k,len(arr)):
            average-=arr[i-k]/k
            average+=arr[i]/k
            if average>=threshold:
                ans+=1
        return ans
solution = Solution()
print(solution.numOfSubarrays([2,2,2,2,5,5,5,8],3,4))