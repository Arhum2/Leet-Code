from typing import List


def longestConsecutive(nums: List[int]) -> int:

### ATTEMPT 1 ###
    # nums.sort()
    # i = 0
    # count = 0
    # while i < len(nums) - 1:
    #     calc = nums[i+1] - nums[i]
    #     i+=1
    #     if calc == 1:
    #         count += 1
    #     elif calc == 0:
    #         count += 0
    #     else:
    #         print(count)
    # return count

        bank = {}
        count = 0
        longest = 0

        if len(nums) == 0:
            return 0

        for num in nums:
            if num not in bank:
                bank[num] = 1
            else:
                bank[num] = bank[num] + 1
        
        for num in bank:
            if num - 1 not in bank:
                count += 1
                while num+1 in bank:
                    count += 1
                    num += 1

                if count > longest:
                    longest = count
                    
                count = 0
        
        return longest

        
longestConsecutive([100,4,200,1,3,2])
