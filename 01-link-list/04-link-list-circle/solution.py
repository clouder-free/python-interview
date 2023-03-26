#! /usr/bin/python

"""
LeetCode 141
"""

class LinkNode(object):
    
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

class Solution(object):
    
    def link_list_circle(self, head: LinkNode) -> LinkNode:
        # set
        nodes = set()
        while head:
            if head in nodes:
                return head
            nodes.add(head)
            head = head.next
        return None
    
    def link_list_circle_2(self, head: LinkNode) -> LinkNode:
        # slow fast pointer
        fast, slow = head, head
        flag = False
        while fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                flag = True
                break
        
        if flag:
            while head and fast:
                if head == fast:
                    return head
                head = head.next
                fast = fast.next
        return None

if __name__ == "__main__":
    n7 = LinkNode(7, None)
    n6 = LinkNode(6, n7)
    n5 = LinkNode(5, n6)
    n4 = LinkNode(4, n5)
    n3 = LinkNode(3, n4)
    n2 = LinkNode(2, n3)
    n1 = LinkNode(1, n2)
    n7.next = n4
    result = Solution().link_list_circle_2(n1)
    print("circle node:{}".format(result.val))