class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        if not heights:
            return
        min_height = min(heights)
        max_area = len(heights) * min_height
        if len(heights) <= 1:
            return max_area
        heights.remove(min_height)
        new_area = self.largestRectangleArea(heights)
        return max(max_area, new_area)
    #
    # def largest_1d(self, heights):
    #     max_height = max(heights)
    #     min_height = min(heights)
    #     max_horizontal = len(heights) * min_height
    #     return max(max_horizontal, max_height)


# print(Solution().largestRectangleArea([2,1,5,6,2,3]))
print(Solution().largestRectangleArea([0, 9]))
print(Solution().largestRectangleArea([0]))
print(Solution().largestRectangleArea([]))
# print(Solution().largestRectangleArea([2,4]))
