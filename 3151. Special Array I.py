class Solution(object):
    def isArraySpecial(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums)==1:
            return True
        for i in range(len(nums)-1):
           if  bin(nums[i])[-1]==bin(nums[i+1])[-1]:
            return False
        return True
