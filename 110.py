# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 노드의 차이가 1을 초과하지 않으면 True, 그렇지 않으면 False
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.diffheight = True

        def dfs(node):
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            if abs(left - right) > 1:
                self.diffheight = False
                return -1

            return max(left, right) + 1

        dfs(root)

        return self.diffheight


            
        




        
        


