class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        n = len(nums)
        i = 0
        while i < n-2 and nums[i] <= 0:
            if i > 0 and nums[i] == nums[i-1]:
                 i += 1
                 continue
            low, high = i+1, n-1
            while low < high:
                sum = nums[i]+ nums[low] + nums[high]
                if sum > 0:
                    high -= 1
                elif sum < 0:
                    low += 1
                else:
                    res.append([nums[i], nums[low], nums[high]])
                    while low< high and nums[low] == nums[low+1]:
                        low +=1
                    while low < high and nums[high] == nums[high -1]:
                        high -= 1
                    low += 1
                    high -=1
            i += 1
        return res        
