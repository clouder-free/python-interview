#! /usr/bin/python

class Solution(object):
    
    def minmum_charge(self, rmb: list[int], total: int) -> int:
        # sort rmb 
        rmb.sort(reverse=True)
        count = 0
        for i in range(0, len(rmb)):
            c = total // rmb[i]
            count += c
            total -= c * rmb[i]
            print("size:{} count:{} left:{}".format(rmb[i], c, total))
        return count

if __name__ == "__main__":
    rmb = [1, 2, 5, 10, 20, 50, 100]
    total = 623
    result = Solution().minmum_charge(rmb=rmb, total=total)
    print("result:{}".format(result))
            