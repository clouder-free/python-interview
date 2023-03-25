#! /usr/bin/python

"""
LeetCode 160
"""

class LinkNode(object):
    
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution(object):
    
    def intersection_of_link_lists(self, headA: LinkNode, headB: LinkNode):
        # Time complexity: O(m+n) Spatial complexity: O(m)
        nodes = set()
        while headA:
            nodes.add(headA)
            headA = headA.next
        
        while headB:
            if headB in nodes:
                return True
            headB = headB.next
        return False
    
    def intersection_of_link_lists_2(self, headA: LinkNode, headB: LinkNode):
        length_a, length_b = 0, 0
        ha, hb = headA, headB
        while ha or hb:
            if ha:
                length_a += 1
                ha = ha.next
            if hb:
                length_b += 1
                hb = hb.next
        # max length
        if length_a > length_b:
            length = length_a
        else:
            length = length_b
        # move a and b
        while length:
            if headA == headB:
                return True
            if length_a >= length:
                headA = headA.next
            if length_b >= length:
                headB = headB.next
            length -= 1
        return False
        

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
    n6 = LinkNode(6, n3)
    n7 = LinkNode(7, n6)
    print_link_list(n1)
    print_link_list(n7)
    result = Solution().intersection_of_link_lists_2(headA=n1, headB=n6)
    print("result:%s\n" % result)
