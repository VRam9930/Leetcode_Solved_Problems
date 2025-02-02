class Solution(object):
    def check(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if sorted(nums)==nums:
            return True
        else:
            l=sorted(nums)
            for i in range(1,len(nums)):
                if nums==(l[i:]+l[:i]):
                    return True
                    break
        return False
