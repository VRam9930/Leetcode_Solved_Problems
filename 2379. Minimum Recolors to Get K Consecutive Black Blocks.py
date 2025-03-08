class Solution(object):
    def minimumRecolors(self, blocks, k):
        """
        :type blocks: str
        :type k: int
        :rtype: int
        """
        # if "B"*k in blocks:
        #     return 0
        # else:
        j=k
        mn=float("inf")
        for i in range(len(blocks)):
            if j>len(blocks):
                break
            else:
                mn=min(blocks[i:j].count("W"),mn)
                j+=1
        return mn





                
            

            







        
