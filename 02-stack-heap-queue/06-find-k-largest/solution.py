#! /usr/bin/python

def findKthLargest(nums: list[int], k: int) -> int:
    # quick sort
    start, end = 0, len(nums)-1
    while True:
        i, j = start, end
        target = nums[i]
        while i < j:
            while i < j and nums[j] > target:
                j -= 1
            nums[i] = nums[j]
            while i < j and nums[i] <= target:
                i += 1
            nums[j] = nums[i]
        nums[i] = target
        if i < len(nums) - k:
            start = i+1
        elif i == len(nums) - k:
            return nums[i]
        else:
            end = i-1

if __name__ == "__main__":
    nums = [3, 2, 1, 5, 6, 4]
    result = findKthLargest(nums=nums, k=4)
    print("result:{}".format(result))