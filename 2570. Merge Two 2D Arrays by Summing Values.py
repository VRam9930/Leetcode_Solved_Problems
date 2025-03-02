class Solution(object):
    def mergeArrays(self, nums1, nums2):
        """
        :type nums1: List[List[int]]
        :type nums2: List[List[int]]
        :rtype: List[List[int]]
        """
        res=[]
        nums1.sort()
        nums2.sort()
        # return nums2
        for i in range(len(nums1)):
            flag=False
            for j in range(len(nums2)):
                if nums1[i][0]==nums2[j][0]:
                    nums1[i][1]+=nums2[j][1]
                    res.append(nums1[i])
                    flag=True
                    break
            if not flag:
                res.append(nums1[i])
        a=len(res)
        for i in range(len(nums2)):
            flag=True
            for j in range(a):
                if nums2[i][0]==res[j][0]:
                    flag=False
                    break
            if flag:
                res.append(nums2[i])
                
                

        
            # if not flag:
            #     res.append(nums1[i])
            #     if i<len(nums2):
            #         res.append(nums2[i])
        return sorted(res)




