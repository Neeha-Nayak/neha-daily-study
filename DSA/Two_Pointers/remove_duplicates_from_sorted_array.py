class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        for num in nums:
            if count == 0 or num != nums[count-1]:
                nums[count] = num
                count += 1
        return count
