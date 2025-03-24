# Leetcode's solution, Approach A:
class Solution:
    # curr(current index) (nums[i]) + x(some number) (nums[j]) = target
    # x(some number) which is nums[j] = target - curr (nums[i])

    # Time complexity: O(n^2)
    # Space complexity: O(1)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0, len(nums)):
            for j in range (i + 1, len(nums)):
                if nums[j] == target - nums[i]:
                    return [i, j]

        return []