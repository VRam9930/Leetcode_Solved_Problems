class Solution(object):
    def clearDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack=[]
        for i in range(len(s)):
            if stack and s[i].isdigit():
                stack.pop()
            else:
                stack.append(s[i])
        return "".join(stack)



