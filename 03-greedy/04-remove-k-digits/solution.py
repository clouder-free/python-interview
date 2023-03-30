#! /usr/bin/python

"""
LeetCode 402
"""

class Solution(object):
    
    def remove_k_digits(self, num: str, k: int) -> str:
        stack = []
        for i in num:
            while stack and stack[-1] > i and k > 0:
                stack.pop()
                k -= 1
            if i != '0' or stack:
                stack.append(i)
        # k != 0
        while stack and k > 0:
            stack.pop()
            k -= 1
        if stack:
            return "".join(stack)
        return "0"

if __name__ == "__main__":
    num = "112"
    k = 1
    result = Solution().remove_k_digits(num, k)
    print("result:{}".format(result))