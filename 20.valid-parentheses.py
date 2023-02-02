#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        s =[i for i in s[0]]
        label =["(",")","[","]","{","}"]
        k = [x for x in s for y in label if x==y]
        if int(len(k))%2!=0:
            return False
        stack=[]
        for i in range(len(s)):
            if s[i]=="(" or s[i]=="[" or s[i]=="{":
               stack.append(s[i])
            elif s[i]==")":
                if stack==[]:
                    return False    
                elif stack.pop()!="(":
                    return False
            elif s[i]=="]":
                if stack==[]:
                    return False    
                elif stack.pop()!="[":
                    return False
            elif s[i]=="}":
                if stack==[]:
                    return False    
                elif stack.pop()!="{":
                    return False
        if stack==[]:
            return True
        else:
            return False
# @lc code=end

