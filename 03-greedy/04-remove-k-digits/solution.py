#! /usr/bin/python

class Solution(object):
    
    def remove_k_digits(self, num: str, k: int) -> str:
        if len(num) == 1:
            return "0"
        stack = []
        for i in num:
            if not stack:
                stack.append(i)
                continue
            # keep stack top or tick off
            if stack[-1] > i and k > 0:
                k -= 1
                # pop element
                stack.pop()
                stack.append(i)
            else:
                stack.append(i)
        if not stack:
            return "0"
        result = "".join(stack).lstrip("0")
        if result:
            return result
        return "0"

if __name__ == "__main__":
    num = "112"
    k = 1
    result = Solution().remove_k_digits(num, k)
    print("result:{}".format(result))