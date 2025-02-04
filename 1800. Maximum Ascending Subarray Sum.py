class Solution(object):
    def maxAscendingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mx=float('-inf')
        for i in range(len(nums)):
            for j in range(i+1,len(nums)+1):
                if len(nums[i:j])==1:
                    mx=max(mx,nums[i])
                elif nums[i:j]==sorted(nums[i:j]) and len(set(nums[i:j])) == len(nums[i:j]):
                    mx=max(mx,sum(nums[i:j]))
        return mx
