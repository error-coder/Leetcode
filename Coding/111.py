# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 최소 깊이 찾기, 최소 깊이는 루트 노드에서 가장 가까운 리프 노드까지 최단 경로를 잇는 노드의 수
# 리프는 하위 항목이 없는 노드

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        # 자식 노드가 한쪽에 없을 경우(왼, 오 나눔)
        if not root.left:
            return self.minDepth(root.right) + 1

        if not root.right:
            return self.minDepth(root.left) + 1
        
        # 자식 노드가 양쪽 다 있을 경우
        else:
            left = 1
            right = 1

            left += self.minDepth(root.left)
            right += self.minDepth(root.right)

        return min(left, right)
        

            
    