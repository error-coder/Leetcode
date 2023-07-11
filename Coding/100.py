# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # p와 q가 같이 None이면 둘다 같으니 True, 둘 중에 하나거 다르면 둘다 같지 않으니 False
        if p is None and q is None:
            return True
        elif p is None or q is None:
            return False
        else:
            # 재귀 활용
            if p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right):
                return True
            else:
                return False
            