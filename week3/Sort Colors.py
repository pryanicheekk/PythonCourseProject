class Solution(object):
    def sortColors(self, nums):
        kolv0 = 0
        kolv1 = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                kolv0 += 1
            elif nums[i] == 1:
                kolv1 += 1
        for i in range(len(nums)):
            if i < kolv0:
                nums[i] = 0
            elif kolv0 <= i < kolv0 + kolv1:
                nums[i] = 1
            else:
                nums[i] = 2