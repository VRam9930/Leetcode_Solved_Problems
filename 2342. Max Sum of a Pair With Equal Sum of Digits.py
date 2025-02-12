class Solution(object):
    def maximumSum(self, nums):
        def digit_sum(n):
            s = 0
            while n > 0:
                s += n % 10
                n //= 10
            return s
        
        digit_map = {}  
        max_sum = -1

        for num in nums:
            d_sum = digit_sum(num)
            if d_sum in digit_map:
                max_sum = max(max_sum, digit_map[d_sum] + num)
                digit_map[d_sum] = max(digit_map[d_sum], num)  
            else:
                digit_map[d_sum] = num 
        
        return max_sum

    # def maximumSum(self, nums):
    #     def digit_sum(n):
    #         s=0
    #         while n>0:
    #             s+=n%10
    #             n=n//10
    #         return s
    #     hashmap={}
    #     for i in range(len(nums)):
    #         hashmap[i]=digit_sum(nums[i])
    #     """
    #     :type nums: List[int]
    #     :rtype: int
    #     """
    #     mx=0
    #     for i in range(len(nums)):
    #         for j in range(i+1,len(nums)):
    #             if hashmap[i]==hashmap[j]:
    #                 mx=max(mx,nums[i]+nums[j])
    #     if mx>0:
    #         return mx
    #     return -1

    
