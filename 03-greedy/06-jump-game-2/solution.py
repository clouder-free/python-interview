#! /usr/bin/python

"""
LeetCode 45
"""

class Solution(object):
    
    def jump(self, nums: list[int]) -> int:
        # dynamic process
        dp = [0] * len(nums)
        for i in range(len(nums)-2, -1, -1):
            if nums[i] == 0:
                dp[i] = len(nums)
            elif i + nums[i] >= len(nums)-1:
                dp[i] = 1
            else:
                dp[i] = min(dp[i+1:i+nums[i]+1]) + 1
        return dp[0]

if __name__ == "__main__":
    nums = [2, 3, 0, 1, 4]
    reuslt = Solution().jump(nums)
    print("result:{}".format(reuslt))
