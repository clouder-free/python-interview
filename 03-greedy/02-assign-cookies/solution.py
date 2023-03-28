#! /usr/bin/python

"""
LeetCode 455
"""

class Solution(object):
    
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        # g demand s cookies
        # sort g and s
        g.sort()
        s.sort()
        i, j = 0, 0
        count = 0
        while i < len(g) and j < len(s):
            if g[i] <= s[j]:
                i += 1
                j += 1
                count += 1
            else:
                j += 1
        return count

if __name__ == "__main__":
    g = [5, 10, 2, 9, 15, 9]
    s = [6, 1, 20, 3, 8]
    result = Solution().findContentChildren(g, s)
    print("count:{}".format(result))
    


