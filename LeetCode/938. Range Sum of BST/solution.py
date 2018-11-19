# url : https://leetcode.com/problems/range-sum-of-bst/
# tag : DFS


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        if root is None:
            return 0
        
        temp = 0
        if L <= root.val <= R:
            temp = root.val        
        # print(root.val, temp)
        return temp + self.rangeSumBST(root.left, L, R) + self.rangeSumBST(root.right, L, R)
    
