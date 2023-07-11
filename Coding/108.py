# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 왼쪽 먼저 방문 후 자기 자신 처리, 오른족 방문 -> Inorder Traversal
# 0이 root노드
from logging import root


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # 예외처리
        if not nums:
            return None

        # 배열을 반으로 쪼개서 인덱스로 만들어 줌
        mid = len(nums) // 2
        # 가운데 값을 기준으로 나눠질 수 있음
        node = TreeNode(nums[mid])
        # 왼쪽 노드에 들어갈 배열은 처음부터 mid까지
        node.left = self.sortedArrayToBST(nums[:mid])
        # 오른쪽 노드는 mid의 다음 인덱스인 mid + 1부터가 마지막 인덱스
        node.right = self.sortedArrayToBST(nums[mid + 1:])

        return node
