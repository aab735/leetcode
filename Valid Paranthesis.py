class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        opened = {'(':1,'{':2,'[':3}
        close = {')':1,'}':2,']':3}
        stack=[]
        if not s:
            return False
        if s=="":
            return True
        if len(s)%2!=0:
            return False
        for i in s:
            if i in opened:
                stack.append(i)
            if i in close:
                if len(stack)>0 and opened.get(stack.pop())==close.get(i):
                    continue
                else:
                    return False
        if len(stack)==0:
            return True
        else:
            return False
string=Solution()
print string.isValid('{}')