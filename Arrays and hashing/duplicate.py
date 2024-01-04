import collections
from typing import List

class Solution:

    def containsDuplicate(self, nums: List[int]) -> bool:
        copy = nums.copy()
        for num in nums:
            copy.remove(num)
            if num in copy.remove(num):
                return True
            else:
                return False

if __name__ == '__main__':
    solution = Solution()
    result = solution.containsDuplicate([1, 2, 3, 1])
    print(result)

