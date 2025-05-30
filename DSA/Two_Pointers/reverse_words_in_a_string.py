class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        l = s.split()
        left, right = 0, len(l)-1
        while left < right:
            l[left], l[right] = l[right], l[left]
            left += 1
            right -=1
        return " ".join(l)
