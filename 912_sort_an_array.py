# Given an array of integers nums, sort the array in ascending order.
from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge_sort(nums):
            n = len(nums)
            if n > 1:
                mid = n // 2
                left = nums[:mid]
                right = nums[mid:]
                merge_sort(left)
                merge_sort(right)
                p = 0
                q = 0
                r = 0
                left_size = len(left)
                right_size = len(right)
                while p < left_size and q < right_size:
                    if left[p] < right[q]:
                        nums[r] = left[p]
                        p += 1
                    else:
                        nums[r] = right[q]
                        q += 1
                    r += 1

                while p < left_size:
                    nums[r] = left[p]
                    p += 1
                    r += 1

                while q < right_size:
                    nums[r] = right[q]
                    q += 1
                    r += 1

        merge_sort(nums)


if __name__ == "__main__":
    nums = [5, 6, 43, -4, 2]
    Solution().sortArray(nums)
    print(nums)
