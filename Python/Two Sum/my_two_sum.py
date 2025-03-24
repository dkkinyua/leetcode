# My Solution
# Approach
"""
My approach is:
We need to get the sum of two indices in an array.
1. Use Cases:
    (i) We cannot get the sum of the same indices i.e. [1, 1]
    (ii) The right index/pointer (L) cannot be behind the left index/pointer (L) i.e. R < L
    (iii) If the right index is at the end of the array, move the left index by one and R should be one index to the right, then the loop continues.

2. How I arrange these:
    (i) Using a while loop, get the sum of the left and right index which start at nums[0] and nums[1] respectively.
    (ii) If the target is not equal to the total calculated, move the right index forward by one. But using a nested loop, if R is at the end of the array, do the third use case
    (iii) If all the above conditions are false, it means that the total is equal to target, so return both indices.

"""
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


        