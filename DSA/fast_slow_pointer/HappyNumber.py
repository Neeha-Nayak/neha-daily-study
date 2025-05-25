class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        slow = n
        fast = self.sum_sqr(n)
        while fast != 1 and slow != fast:
            slow = self.sum_sqr(slow)
            fast = self.sum_sqr(self.sum_sqr(fast))
        return fast == 1
    
    def sum_sqr(self,n):
        digits = str(n)
        return sum(int(digit)**2 for digit in digits)
