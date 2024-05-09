import collections
from typing import List

# class Solution:

#     def containsDuplicate(self, nums: List[int]) -> bool:
#         for num in nums:
#             if nums.count(num) > 1:
#                 return True
#         return False

# too slow ^
    
# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:

#         dict = {}
        
#         for num in nums:
#             if num not in dict:
#                 dict[num] = 0
#             else:
#                 return True
#         return False

# used a hashmap lol

def containsDuplicate(nums: List[int]) -> bool:
    for num in nums:
        temp_num = nums.remove(num)
        if num in nums:
            return True
    return False

#run this code on [1,2,1]

if __name__=="__main__":
    # s = Solution()
    containsDuplicate([274,-735,-911,80,454,-511,922,-775,985,-669,-463,-896,-629,-586,910,-361,288,-375,88,556,-578,-406,-87,25,377,-635,-445,-289,646,-962,-487,-924,-968,-962,502,36,129,-611,54,-27,-496,915,-84,-782,349,678,332,-114,345,14,119,710,821,-194,988,38,-369,409,-559,-529,-298,-593,705])

# Crappier solution
# the reason this solution fails sometimes is because the for loop skips a value when it removes a value from the list