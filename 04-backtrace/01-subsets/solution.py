#! /usr/bin/python

class Solution(object):
    
    def subsets(self, nums: list[int]) -> list[list[int]]:
        result = [[]]
        for num in nums:
            res = result[:]
            for r in res:
                r.append(num)
            print("res:{}".format(res))
            result.append(res[:])
            print(result)
        return result

if __name__ == "__main__":
    nums = [1, 2, 3]
    result = Solution().subsets(nums)
    s = "test"
    s.isdigit()
    s.isalpha()
    
    
    
    
    print(result)
