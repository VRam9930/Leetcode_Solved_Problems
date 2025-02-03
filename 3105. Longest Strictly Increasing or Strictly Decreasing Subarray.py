class Solution(object):
    def longestMonotonicSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0  

        inc = dec = max_length = 1
        
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:  
                inc += 1
                dec = 1
            elif nums[i] < nums[i - 1]:  
                dec += 1
                inc = 1
            else:  
                inc = dec = 1

            max_length = max(max_length, inc, dec) 

        return max_length
