class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # counter = 0
        # counter1 = 1

        # for num in nums:
        #     for num1 in nums[1:]:
        #         if (num + num1) == target:
        #             return [counter, counter1]

        #     counter1 += 1
        #     counter += 1

        for i in range(len(nums)):
            for j in range(len(nums)):
                if (nums[i] + nums[j]) == target:
                    if j != i:
                        return [i, j]