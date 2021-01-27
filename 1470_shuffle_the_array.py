# Given the array nums consisting of 2n elements in the form
# [x1,x2,...,xn,y1,y2,...,yn].
# Return the array in the form [x1,y1,x2,y2,...,xn,yn].
from typing import List


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        new_nums = []
        for i in range(n):
            new_nums.extend((nums[i], nums[i+n]))
        return new_nums


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 4, 3, 2, 1]
    n = 3
    print(Solution().shuffle(nums, n))
