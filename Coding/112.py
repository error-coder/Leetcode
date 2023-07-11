# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 트리의 경로를 탔을 때 targetSum을 만들 수 있는 지 만들 수 있다면 
# 해당 노드가 뿌리노드까지 닿은건지 확인하여 return합니다.
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node):
            if not root:
                return False

            left = dfs(node.left)
            right = dfs(node.right)

            