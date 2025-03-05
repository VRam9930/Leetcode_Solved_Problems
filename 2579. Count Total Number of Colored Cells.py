class Solution(object):
    def coloredCells(self, n):
        """
        :type n: int
        :rtype: int
        """
        s=1
        for i in range(1,n):
            s+=4*i
        return s
