#First solution:
# class Solution:
#     def twoSum(self, numbers: List[int], target: int) -> List[int]:
#         start = 0
#         end = len(numbers) - 1
#         flag = False

#         while not flag:
#             result = target - (numbers[end] + numbers[start])
#             if result == 0:
#                 flag = True
#                 return([start+1, end+1])
#             elif result < 0:
#                 end -= 1
#             elif result > 0:
#                 start += 1
#             elif start == end:
#                 flag = True
#                 return []

#Second solution (just uses less lines):        
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start = 0
        end = len(numbers) - 1
        flag = False

        while not flag:
            result = target - (numbers[end] + numbers[start])
            if result == 0:
                flag = True
                return([start+1, end+1])
            elif result < 0:
                end -= 1
            else:
                start += 1
