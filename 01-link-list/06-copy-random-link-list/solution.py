#! /usr/bin/python

"""
LeetCode 138
"""

class LinkNode(object):
    
    def __init__(self, val, next: "LinkNode"=None, random: "LinkNode"=None):
        self.val = val
        self.next = next
        self.random = random

class Solution(object):
    
    def copy_random_list(self, head: LinkNode) -> LinkNode:
        # traverse link list
        new_head = LinkNode(0)
        p, q = head, new_head
        random_dict = {}
        while p:
            node = LinkNode(p.val)
            q.next = node
            q = q.next
            # node and new_node map
            random_dict[p] = node
            p = p.next
        q = new_head.next
        while head:
            if head.random:
                q.random = random_dict[head.random]
            head = head.next
            q = q.next
        return new_head.next

def print_random_link_list(head: LinkNode):
    print("{} random:{}".format(head.val, head.random.val if head.random else None), end="")
    while head.next:
        print("->", end="")
        head = head.next
        print("{} random:{}".format(head.val, head.random.val if head.random else None), end="")
    print()

if __name__ == "__main__":
    n5 = LinkNode(5, None, None)
    n4 = LinkNode(4, n5, None)
    n3 = LinkNode(3, n4, None)
    n2 = LinkNode(2, n3, None)
    n1 = LinkNode(1, n2, None)
    n1.random = n3
    n2.random = n4
    n3.random = n3
    n5.random = n4
    print_random_link_list(n1)
    head = Solution().copy_random_list(n1)
    print_random_link_list(head)
    