# Given an array of integers nums.
# A pair (i,j) is called good if nums[i] == nums[j] and i < j.
# Return the number of good pairs.
from typing import List


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        pairs = 0
        repeats = {}
        for i in nums:
            if i not in repeats:
                repeats[i] = 0
            repeats[i] += 1
        for i in repeats:
            n = repeats[i]
            pairs += (n*(n-1)//2)
        return pairs


if __name__ == "__main__":
    nums = [1, 2, 3, 1, 1, 3]
    print(Solution().numIdenticalPairs(nums))
