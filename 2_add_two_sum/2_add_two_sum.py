from node import Node
from listnode import ListNode
from autoGenIntList import AutoGenIntList


class Solution(object):
    def addTwoNumbers(self, list1, list2):
        ret = ListNode()
        carry = 0
        current = ret
        while(list1 is not None or list2 is not None):
            val1 = list1.val if list1 is not None else 0
            val2 = list2.val if list2 is not None else 0
            sum = val1 + val2 + carry
            carry = 1 if sum >= 10 else 0
            sum = sum - 10 if sum >= 10 else sum
            current.addNode(sum)
            list1 = list1.next if list1 is not None else None
            list2 = list2.next if list2 is not None else None
        if carry is 1:
            current.addNode(1)
        return ret
"""Test Code"""
AgList1 = AutoGenIntList(0, 1000)
#AgList1.setNumber(1)
AgList1.genIntList()
print(AgList1.list)
AgList2 = AutoGenIntList(0, 1000)
#AgList2.setNumber(99)
AgList2.genIntList()
print(AgList2.list)
print(Solution().addTwoNumbers(AgList1.list.getStartNode(), AgList2.list.getStartNode()))
