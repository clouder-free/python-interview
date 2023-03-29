#! /usr/bin/python

class Solution(object):
    
    def wiggleMaxLength(self, nums: list[int]) -> int:
        n = len(nums)
        if n < 2:
            return n
        
        prev = nums[1] - nums[0]
        ret = (2 if prev != 0 else 1)
        for i in range(2, n):
            diff = nums[i] - nums[i - 1]
            if (diff > 0 and prev <= 0) or (diff < 0 and prev >= 0):
                ret += 1
                prev = diff
        
        return ret

if __name__ == "__main__":
    nums = [1, 7, 4, 9, 2, 5]
    result = Solution().wiggleMaxLength(nums)
    print(result)