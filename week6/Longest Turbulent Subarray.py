class Solution(object):
    def maxTurbulenceSize(self, arr):
        if len(arr) == 1:
            return 1
        string = ''
        if arr[0] > arr[1]:
            string = 'more'
            result = 2
            max_result = 2
        elif arr[0] < arr[1]:
            string = 'less'
            result = 2
            max_result = 2
        else:
            string = 'equal'
            result = 1
            max_result = 1
        for i in range(1, len(arr) - 1):
            if (arr[i] > arr[i + 1] and string == 'less') or (arr[i] < arr[i + 1] and string == 'more'):
                result += 1
                max_result = max(result, max_result)
                if arr[i] > arr[i + 1]:
                    string = 'more'
                else:
                    string = 'less'
            elif arr[i] > arr[i + 1]:
                result = 2
                max_result = max(result, max_result)
                string = 'more'
            elif arr[i] < arr[i + 1]:
                result = 2
                max_result = max(result, max_result)
                string = 'less'
            else:
                result = 1
                string = 'equal'
        return max_result
solution = Solution()
print(solution.maxTurbulenceSize([9,4,2,10,7,8,8,1,9]))