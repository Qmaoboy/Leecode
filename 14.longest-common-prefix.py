#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        def main(self,data):
            if len(data) < 2:
                return ""
            else:
                final =[i for i in data[0]]
                for idx in range(1,len(data)):
                    if final==[]:
                        break
                    final =self.compare(final,[i for i in data[idx]])
            symbo =""
            final =symbo.join(final)
            return final
        def compare(self,d1,d2):
            j=0
            for k in range(len(d2)):
                if d1[j]==d2[k]:
                    j +=1
                    if j ==len(d1):
                        return d1
                else:
                    break
            return d1[:j]
# @lc code=end

