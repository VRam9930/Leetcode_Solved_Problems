class Solution(object):
    def tupleSameProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        count = collections.Counter()

        for i in range(len(nums)):
            for j in range(i):
                prod = nums[i] * nums[j]
                ans += count[prod] * 8
                count[prod] += 1
        return ans
