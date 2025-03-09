class Solution(object):
    def numberOfAlternatingGroups(self, colors, k):
        """
        :type colors: List[int]
        :type k: int
        :rtype: int
        """
        colors.extend(colors[:(k-1)])  
        count = 0
        left = 0

        for right in range(len(colors)):
            if right > 0 and colors[right] == colors[right - 1]:
                left = right  
            
            if right - left + 1 >= k:
                count += 1  
        
        return count
#         r=0
#         j=k
#         for i in range(len(colors)):
#             c=0
#             for x in range(i,j-1):
#                 if colors[x+1]==colors[x]:
#                     break
#                 else:
#                     c+=1
#             if c==k-1:
#                 r+=1
#             j+=1
#             if j>len(colors)-1:
#                 j=j%len(colors)-1
#         return r
#             # j=(j+k)%len(colors)

             




            

        
