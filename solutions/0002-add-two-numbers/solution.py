# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
ListNode라는 클레스를 다룸.
기본적으로 임시 노드를 설정(dummy = ListNode(0))하고 뒤에 Head를 붙임.
이후 curr = dummy로 커서를 따로 분리해서 사용.
값을 추가할 때에는 curr.next = ListNode(val)로 추가하고 curr = curr.next로 커서를 업데이트.
값을 반환할 때에는 dummy.next로 커서를 Head로 이동.
값을 출력할 때에는 dummy.val로 가져옴.
"""
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        total = 0
        dummy = ListNode(0)
        curr = dummy

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total += val1 + val2 + carry
            curr.next = ListNode(total % 10)
            curr = curr.next           
            carry = total // 10
            total = 0

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next


