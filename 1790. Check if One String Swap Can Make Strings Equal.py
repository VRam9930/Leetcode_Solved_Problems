class Solution(object):
    def areAlmostEqual(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        t=list(s1)
        n=list(s2)
        if t==n:
            return True
        # elif len(set(t))==len(set(n)):
        #     return True
        for i in range(len(s1)):
            c1=s1.count(t[i])
            c2=s2.count(t[i])
            if c1!=c2:
                return False
        for i in range(len(s1)):
            for j in range(i+1,len(s1)):
                t1=t[:]
                t1[i],t1[j]=t1[j],t1[i]
                # print(t)
                # print(t1)
                if t1==n:
                    return True
        return False

        
