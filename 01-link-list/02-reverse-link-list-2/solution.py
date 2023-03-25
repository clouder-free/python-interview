#! /usr/bin/python

"""
LeetCode 92
"""

class LinkNode(object):
    
    def __init__(self, val, next=None) -> None:
        self.val = val
        self.next = next

class Solution(object):
    
    def reverse_link_list_between(self, head:LinkNode, m:int, n:int) -> LinkNode:
        length = n - m + 1
        h, l = head, None
        while m-1:
            l = h
            h = h.next
            m -= 1
        
        # reverse start
        tail = h
        nh = None
        while length:
            p = h.next
            h.next = nh
            nh = h
            h = p
            length -= 1
        if l:
            l.next = nh
        else:
            head = nh
        tail.next = h
        return head

def print_link_list(head: LinkNode):
    print(head.val, end="")
    while head.next:
        print("->", end="")
        head = head.next
        print(head.val, end="")
    print()


if __name__ == "__main__":
    n5 = LinkNode(5, None)
    n4 = LinkNode(4, n5)
    n3 = LinkNode(3, n4)
    n2 = LinkNode(2, n3)
    n1 = LinkNode(1, n2)
    print_link_list(n1)
    head = Solution().reverse_link_list_between(head=n1, m=1, n=5)
    print_link_list(head)

            

