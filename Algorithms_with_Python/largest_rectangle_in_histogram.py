class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        if not heights:
            return

        max_area = self.largest_1d(heights)


        for idx in range(len(heights)):
            curr_num = heights[idx]
            for right in range(idx, len(heights)):
                curr_list = [heights[i] for i in range(idx, right+1)]
                curr_min = min(curr_list)
                if curr_min * len(heights) <= max_area:
                    break
                curr_sum = curr_min * (len(curr_list))
                if curr_sum > max_area:
                    max_area = curr_sum
            for left in range(idx, 0, -1):
                curr_list = [heights[i] for i in range(idx, left-2, -1)]
                curr_min = min(curr_list)
                if curr_min * len(heights) <= max_area:
                    break
                curr_sum = curr_min * (len(curr_list))
                if curr_sum > max_area:
                    max_area = curr_sum
        return max_area

    def largest_1d(self, heights):
        max_height = max(heights)
        min_height = min(heights)
        max_horizontal = len(heights) * min_height
        return max(max_horizontal, max_height)


print(Solution().largestRectangleArea([2,1,5,6,2,3]))
print(Solution().largestRectangleArea([0, 9]))
print(Solution().largestRectangleArea([0]))
print(Solution().largestRectangleArea([]))
print(Solution().largestRectangleArea([2,4]))
print(Solution().largestRectangleArea([2, 0, 2]))
from time import time
time1 = time()
print(Solution().largestRectangleArea(asd))
time1 = time() - time1
print(time1)
