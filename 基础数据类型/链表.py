
"""
在链表中删除一个元素
https://leetcode.com/problems/delete-node-in-a-linked-list/
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        nextnode=node.next
        after_next_node=nextnode.next
        node.val=nextnode.val
        node.next=after_next_node

"""
反转链表
https://leetcode.com/problems/reverse-linked-list/
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        pre = None
        cur = head
        while cur:
            nextnode = cur.next
            cur.next = pre
            pre = cur
            cur = nextnode
        return pre

"""
合并两个有序的链表
https://leetcode.com/problems/merge-two-sorted-lists/
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        root=ListNode(None)
        cur=root
        while l1 and l2:
            if l1.val<l2.val:
                node=ListNode(l1.val)
                l1=l1.next
            else:
                node=ListNode(l2.val)
                l2=l2.next
            cur.next=node
            cur=node
        #l1或者l2可能还有剩余元素
        cur.next=l1 or l2
        return root.next