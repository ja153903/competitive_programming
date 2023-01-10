class Solution:
    def findBuildings(self, heights: list[int]) -> list[int]:
        # we can keep track of the largest element we've seen so far
        res = []
        max_height = 0

        for i in range(len(heights) - 1, -1, -1):
            if not res or heights[i] > max_height:
                max_height = heights[i]
                res.append(i)

        res.reverse()

        return res
