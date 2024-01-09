import collections
from typing import List

# class Solution:

#     def containsDuplicate(self, nums: List[int]) -> bool:
#         for num in nums:
#             if nums.count(num) > 1:
#                 return True
#         return False

# too slow ^
    
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        dict = {}
        
        for num in nums:
            if num not in dict:
                dict[num] = 0
            else:
                return True
        return False

# used a hashmap lol