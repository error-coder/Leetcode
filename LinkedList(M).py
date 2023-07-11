# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def removeNthFromEnd(self, head, n):
        cur = head
        arr = []

        # 1. 연결리스트를 어떻게 순회할 것인가?
        while cur != None:
            arr.append(cur)
            cur = cur.next

        # 2. 현재 특정 위치를 어떻게 알 수 있는가?
        targetIdx = len(arr) - n

        # 3. 노드를 어떻게 삭제할 수 있나?
