# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next



class Solution:
    def deleteDuplicates(self, head):
        cur = head

        while cur and cur.next:
            if cur.val == cur.next.val:
                # 값이 중복될 경우 무시하고 넘어가버림
                cur.next = cur.next.next
            else:
                cur = cur.next

        return head


        