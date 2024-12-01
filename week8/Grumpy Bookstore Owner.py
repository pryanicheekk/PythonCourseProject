class Solution(object):
    def maxSatisfied(self, customers, grumpy, minutes):
        answer = 0
        for i in range(len(customers)):
            if grumpy[i]==0:
                answer+=customers[i]
        max_save = 0
        for i in range(minutes):
            max_save+=customers[i]*grumpy[i]
        save = max_save
        for i in range(minutes,len(customers)):
            save +=customers[i]*grumpy[i]
            save -=customers[i-minutes]*grumpy[i-minutes]
            max_save = max(max_save,save)
        return answer + max_save
solution = Solution()
print(solution.maxSatisfied([1,0,1,2,1,1,7,5], [0,1,0,1,0,1,0,1], 3))