#! /usr/bin/python

class LinkNode(object):
    
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

class Solution(object):
    
    def merge_k_sorted_link_list(self, lists) -> LinkNode:
        # merge sort
        return self.merge(lists, 0, len(lists)-1)
    
    def merge(self, lists, i, j) -> LinkNode:
        if i == j:
            return lists[i]
        mid = (i+j) // 2
        left = self.merge(lists, i, mid)
        right = self.merge(lists, mid+1, j)
        return self.merge_sorted_link_list(left, right)
    
    def merge_sorted_link_list(self, l1: LinkNode, l2: LinkNode):
        if not l1:
            return l2
        if not l2:
            return l1
        if l1.val < l2.val:
            l1.next = self.merge_sorted_link_list(l1.next, l2)
            return l1
        else:
            l2.next = self.merge_sorted_link_list(l1, l2.next)
            return l2

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
    print_link_list(n1)
    
    n6 = LinkNode(5, None)
    n5 = LinkNode(3, n6)
    n4 = LinkNode(2, n5)
    print_link_list(n4)
    
    n9 = LinkNode(7, None)
    n8 = LinkNode(5, n9)
    n7 = LinkNode(3, n8)
    print_link_list(n7)
    
    lists = [n1, n4, n7]
    head = Solution().merge_k_sorted_link_list(lists=lists)
    print_link_list(head)
    