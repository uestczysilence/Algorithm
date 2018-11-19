# url : https://leetcode.com/problems/3sum-with-multiplicity/
# tag : math,dp

# 枚举所有加起来等于 target 的组合


class Solution:
    def threeSumMulti(self, A, target):
        """
        :type A: List[int]
        :type target: int
        :rtype: int
        """
        N = 103
        Mod = 1000000007
        cnt = [0] * N
        for i in A:
            cnt[i] += 1
        ret = 0
        # print(cnt)
        for i in range(N):
            if i * 3 == target:
                ret += cnt[i] * (cnt[i]-1) * (cnt[i]-2) // 6
                ret %= Mod
            

            for j in range(i+1, N):
                if i*2+j == target:
                    ret += cnt[i] * (cnt[i]-1) // 2 * cnt[j]
                    ret %= Mod


                if i+j*2 == target:
                    ret += cnt[i] * cnt[j] * (cnt[j]-1) // 2 
                    ret %= Mod   
                
                for k in range(j+1, N):
                    if i+j+k == target:
                        ret += cnt[i] * cnt[j] *cnt[k]
                        ret %= Mod
        
        return ret




s = Solution()
print(s.threeSumMulti([1,1,2,2,3,3,4,4,5,5], 8))
print(s.threeSumMulti([1,1,2,2,2,2], 5))
print(s.threeSumMulti([3,3,1], 7))





