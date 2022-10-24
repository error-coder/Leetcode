# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right\

# 이진 트리의 루트가 주어지면 최대 깊이를 반환합니다. 
# 바이너리 트리의 최대 깊이는 루트 노드에서 가장 먼 리프 노드까지 가장 긴 경로를 따라 있는 노드의 수입니다.
# 재귀를 활용하여 푸는게 좋아보임(다시 돌아가서 확인해야 되기 때문)
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0

        # 깊이를 구하는 문제이고 왼쪽, 오른쪽을 다 탐색후 오른쪽에 자식 노드들이 더 있기 때문에 길이를 더해줌
        # 오른쪽에만 더해주면 되는줄 알았는데 테스트케이스 [1,null,2]에서 output이 [2]이기 때문에
        # 1에 자식 노드가 달려있다는 얘기고 그 다음 깊이를 탐색한 후 2가 도출되었으므로 양쪽에다 1을 더해줘야된다.
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

# 다양한 방법으로 풀 수 있음(스택, 큐 등 활용 가능)