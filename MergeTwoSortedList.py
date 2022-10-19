# Definition for singly-linked list.
from platform import node

class ListNode:
     def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



class Solution:
    def mergeTwoLists(self, l1, l2):
        # 헤더와 노드 선언
        head = ListNode(0)
        tail = node

        # l1과 l2값을 비교해 작은 값부터 추가해주는 방식
        while l1 and l2:
            if l1.val <= l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            # 업데이트를 해줘야함
            tail = tail.next
        # l1과 l2의 길이가 다른 경우 소진되는 리스트가 있을 수도 있기 때문에 남은 부분을 연결해주는 코드
        tail.next = l1 or l2

        return node.next
