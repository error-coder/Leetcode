# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head):
        cur = head
        prevNode = None
        nextNode = None

        while cur:
            nextNode = cur.next  # cur의 다음 주소
            cur.next = prevNode  # nextNode를 prevNode에 연결
            prevNode = cur  # 반대 방향으로 이동
            cur = nextNode  # cur도 이동

        return prevNode
