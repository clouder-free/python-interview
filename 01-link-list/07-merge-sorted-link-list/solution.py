#! /usr/bin/python

"""
LeetCode 21
"""

class LinkNode(object):
    
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

class Solution(object):
    
    def merge_two_sorted_list(self, l1: LinkNode, l2: LinkNode) -> LinkNode:
        head = LinkNode(0)
        tail = head
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        if l1:
            tail.next = l1
        if l2:
            tail.next = l2
        return head.next

def print_link_list(head: LinkNode):
    print(head.val, end="")
    while head.next:
        print("->", end="")
        head = head.next
        print(head.val, end="")
    print()

if __name__ == "__main__":
    n3 = LinkNode(3, None)
    n2 = LinkNode(2, n3)
    n1 = LinkNode(1, n2)
    n6 = LinkNode(5, None)
    n5 = LinkNode(3, n6)
    n4 = LinkNode(2, n5)
    print_link_list(n1)
    print_link_list(n4)
    head = Solution().merge_two_sorted_list(n1, n4)
    print_link_list(head)
    
    