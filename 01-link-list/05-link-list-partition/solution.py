#! /usr/bin/python

"""
LeetCode 86
"""

class LinkNode(object):
    
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

class Solution(object):
    
    def link_list_partition(self, head: LinkNode, x: int) -> LinkNode:
        lower_head, higher_head = LinkNode(0), LinkNode(0)
        lower_tail, higher_tail = lower_head, higher_head
        while head:
            if head.val < x:
                lower_tail.next = head
                lower_tail = lower_tail.next
            else:
                higher_tail.next = head
                higher_tail = higher_tail.next
            head = head.next

        if lower_head.next:
            lower_tail.next = higher_head.next
            higher_tail.next = None
            return lower_head.next
        else:
            return higher_head.next

def print_link_list(head: LinkNode):
    print(head.val, end="")
    while head.next:
        print("->", end="")
        head = head.next
        print(head.val, end="")
    print()

if __name__ == "__main__":
    n5 = LinkNode(1, None)
    n4 = LinkNode(4, n5)
    n3 = LinkNode(3, n4)
    n2 = LinkNode(2, n3)
    n1 = LinkNode(5, n2)
    n6 = LinkNode(2, n1)
    print_link_list(n6)
    result = Solution().link_list_partition(n6, x=3)
    print_link_list(result)
        
        