# My Solution
# Time Complexity = O(N)
# Space Complecity = O(1)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        L = 0
        R = 0 + 1

        while L < R and R != n:
            total = nums[L] + nums[R]

            if total != target:
                R += 1
                if R == n:
                    L += 1
                    R = L + 1

            else:
                return L, R

        return L, R


        