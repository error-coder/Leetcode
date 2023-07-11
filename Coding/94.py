# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 2. 중위 순회(Inorder Traversal)
#     - 왼쪽 자식을 방문한다.
#     - 먼저 자기 자신을 처리한다.
#     - 오른쪽 자식을 방문한다.

class Solution:
    def inorderTraversal(self, root):
        result = []
        
        # dfs라는 중위 순회하는 함수를 따로 만든다
        def dfs(node):
            # 노드가 방문후 아무것도 없으면 반환X
            if node is None:
                return None

            # 중위 순회는 왼족 -> 자기 자신 처리 후 -> 오른쪽 방문임
            dfs(node.left)
            # 왼쪽 방문 후 처리한 값을 결과 스택에 넣어준다.
            result.append(node.val)
            # 그 다음 오른쪽을 방문
            dfs(node.right)

        dfs(root)

        return result


            

            
            

