# url : https://leetcode.com/problems/di-string-match/
# tag : constructive algorithm

# 值域是[0,len(S)]
# 遇到 I 就写最大的数字
# 遇到 D 就写最小的数字
# 然后反转连续的相同字母段
# 显而易见是正确的


class Solution:
    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        max = len(S)
        min = 0
        S += 'Z'
        ret = []
        if S[0] == 'I':
            ret.append(0)
            min+=1
        elif S[0] == 'D':
            ret.append(max)
            max-=1

        start, cur = 0, 0
        tempRet = []
        for si in S:
            if si != S[start]:
                start = cur
                tempRet.reverse()
                ret += tempRet
                tempRet = []
            if si == 'I':
                tempRet.append(max)
                max-=1
            elif si == 'D':
                tempRet.append(min)
                min+=1    
            cur += 1
        return ret
            


s = Solution()
print(s.diStringMatch('IDID'))
print(s.diStringMatch('III'))
print(s.diStringMatch('DDI'))




