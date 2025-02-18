class Solution(object):
    def smallestNumber(self, pattern):
        """
        :type pattern: str
        :rtype: str
        """
        s=pattern
        return min(''.join(p) for p in permutations('123456789'[:len(s)+1]) if all((gt,lt)[q=='I'](*p[i:i+2]) for i,q in enumerate(s)))
