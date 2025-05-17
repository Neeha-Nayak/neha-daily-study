class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # n = len(nums)
        # for i  in range(n):
        #     min_index = i
        #     j = i + 1
        #     while j < n:
        #         if nums[min_index] >nums[j]:
        #             min_index = j
        #         j += 1
        #     nums[i], nums[min_index] = nums[min_index], nums[i]
        # return nums

        ### Dutch National Flag algorithm
        start, current, end = 0, 0, len(nums) - 1
        while current <= end:
            if nums[current] == 0:
                nums[start] , nums[current] = nums[current], nums[start]
                current += 1
                start +=1
            elif nums[current] == 2:
                nums[end] , nums[current] = nums[current], nums[end]
                end -= 1
            else:
                current += 1
        return nums
