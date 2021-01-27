# Given the array nums, for each nums[i] find out how many
# numbers in the array are smaller than it.
# That is, for each nums[i] you have to count the number of valid j's
# such that j != i and nums[j] < nums[i].
# Return the answer in an array.
from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        new_nums = [*nums]
        index = 0
        for i in nums:
            count = 0
            for j in nums:
                if i > j:
                    count += 1
            new_nums[index] = count
            index += 1

        return new_nums


if __name__ == "__main__":
    nums = [8, 1, 2, 2, 3]
    print(Solution().smallerNumbersThanCurrent(nums))
