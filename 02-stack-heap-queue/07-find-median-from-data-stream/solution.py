#! /usr/bin/python

"""
LeetCode 295
"""

class MedianFinder(object):
    
    def __init__(self):
        self.nums = []
    
    def addNum(self, num: int) -> None:
        i, j = 0, len(self.nums)
        while i < j:
            m = (i+j)//2
            if self.nums[m] == num:
                i = m
                break
            elif self.nums[m] > num:
                j = m-1
            else:
                i = m+1
        self.nums = self.nums[:i] + [num] + self.nums[i:]
    
    def findMedian(self) -> float:
        m = len(self.nums) // 2
        if len(self.nums) % 2 == 0:
            return (self.nums[m]+self.nums[m-1])/2
        else:
            return self.nums[m]

if __name__ == "__main__":
    finder = MedianFinder()
    finder.addNum(1)
    print("nums:{}".format(finder.nums))
    print("median:{}".format(finder.findMedian()))
    finder.addNum(2)
    print("nums:{}".format(finder.nums))
    print("median:{}".format(finder.findMedian()))
    finder.addNum(3)
    print("nums:{}".format(finder.nums))
    print("median:{}".format(finder.findMedian()))