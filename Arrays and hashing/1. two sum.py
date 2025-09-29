class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        bank = {}
        i = 0

        for num in nums:
            if target-num in bank:
                return [bank[target - num], i]
            else:
                bank[num] = i
            
            i+=1
            