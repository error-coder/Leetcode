# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def dfs(left, right):
            if left is None and right is None:
                return True
            elif left is None or right is None:
                return False
            # 대칭이 되야 하니 맨 왼쪽 노드와 맨 오른족 노드 비교후 나머지 노드 비교
            else:
                return left.val == right.val and dfs(left.left, right.right) and dfs(left.right, right.left)

        return dfs(root, root)