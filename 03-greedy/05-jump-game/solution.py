#! /usr/bin/python

"""
LeetCode 55
"""

class Solution(object):
    
    def canJump(self, nums: list[int]) -> bool:
        max_pos = 0
        for i in range(len(nums)):
            if max_pos < i:
                continue
            max_pos = max(max_pos, i+nums[i])
            if max_pos >= len(nums) - 1:
                return True
        return False

if __name__ == "__main__":
    nums = [3, 2, 1, 0, 4]
    reuslt = Solution().canJump(nums=nums)
    print("result:{}".format(reuslt))
