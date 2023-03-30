#! /usr/bin/python

class Solution(object):
    
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        if len(points) == 1:
            return 1
        # sort by point[0]
        points = sorted(points, key=lambda point: point[0])
        # print(points)
        result = 1
        scale = points[0]
        for i in range(1, len(points)):
            if points[i][0] <= scale[1]:
                scale[0] = points[i][0]
                if points[i][1] <= scale[1]:
                    scale[1] = points[i][1]
            else:
                result += 1
                scale = points[i]
        return result

if __name__ == "__main__":
    points = [[10,16],[2,8],[1,6],[7,12]]
    result = Solution().findMinArrowShots(points=points)
    print("result:{}".format(result))