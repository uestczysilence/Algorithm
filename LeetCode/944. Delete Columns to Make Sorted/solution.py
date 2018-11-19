# url : https://leetcode.com/problems/delete-columns-to-make-sorted/
# tag : brute force

# 删除几列使得剩下的字符串数组不降序
# 简单循环
# (扩展) 删除几列使得剩下的字符串数组不降序，经典 LIS



class Solution:
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """

        la = len(A)
        l = len(A[0])
        ret = 0
        for i in range(l):
            for j in range(1, la):
                if A[j-1][i] > A[j][i]:
                    # print('i = {}, j = {}, A[j][i] = {}, A[j-1][i] = {}'.format( i, j, A[j][i], A[j-1][i]))
                    ret+=1
                    break
    
        return ret


s = Solution()
print(s.minDeletionSize(["cba","daf","ghi"]))
print(s.minDeletionSize(["a","b"]))
print(s.minDeletionSize(["zyx","wvu","tsr"]))




