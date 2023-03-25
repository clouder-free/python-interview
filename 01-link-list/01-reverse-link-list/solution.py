#! /usr/bin/python
# -*- encoding: utf-8 -*-

"""
LeetCode 206
"""

class LinkNode(object):
    
    def __init__(self, val, next):
        self.val = val
        self.next = next

class Solution(object):
    
    def reverse_link_list(self, head: LinkNode) -> LinkNode:
        fake = LinkNode(0, None)
        while head:
            p = head.next
            head.next = fake.next
            fake.next = head
            head = p
        return fake.next

def traverse_link_list(head: LinkNode):
    while head:
        print(head.val, end="")
        if head.next:
            print("->", end="")
        head = head.next
    print()

if __name__ == "__main__":
    n5 = LinkNode(5, None)
    n4 = LinkNode(4, n5)
    n3 = LinkNode(3, n4)
    n2 = LinkNode(2, n3)
    n1 = LinkNode(1, n2)
    traverse_link_list(n1)
    head = Solution().reverse_link_list(n1)
    traverse_link_list(head)



